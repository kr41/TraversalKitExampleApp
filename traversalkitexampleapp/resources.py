import math

from pyramid.decorator import reify
from traversalkit import Resource, DEC_ID, TEXT_ID

from . import models


def root_factory(request):
    return SiteRoot()


class SiteRoot(Resource):
    """ Root resource of the site """

    title = 'TraversalKit Example Application'


@SiteRoot.mount('authors')
class Authors(Resource):
    """ Collection of site authors """

    title = 'Authors'

    def all(self, ids=None):
        """ Returns iterator over the authors """
        session = models.DBSession()
        query = session.query(models.Author)
        if ids:
            query = query.filter(models.Author.id.in_(ids))
        for author in query.all():
            yield self.get(author.username, author)

    def by_id(self, id):
        """ Loads Author resource by ID """
        session = models.DBSession()
        query = session \
            .query(models.Author) \
            .filter(models.Author.id == id)
        author = query.one()
        return self.get(author.username, author)


@Authors.mount_set(TEXT_ID)
class Author(Resource):
    """ Authors resource """

    # Parent resource (Authors) should catch this exception and turn it
    # to KeyError.  It is needed to raise "404 Not Found" instead of
    # "500 Internal Server Error".
    __not_exist__ = models.NoResultFound

    def on_init(self, author):
        """ Load author profile from database if it has not been loaded """
        if author is None:
            session = models.DBSession()
            query = session \
                .query(models.Author) \
                .filter(models.Author.username == self.__name__)
            author = query.one()
        self.id = author.id
        self.title = self.name = author.name
        self.about = author.about


@SiteRoot.mount('blog')
@Author.mount('articles')
class Blog(Resource):
    """ Blog resource """

    page_len = 5

    @reify
    def title(self):
        # If Blog resource has Author one in its lineage,
        # resource title will be "Articles".  Otherwise, "Blog" will be used.
        return 'Articles' if self.parent(cls=Author) else 'Blog'

    def page(self, num):
        """ Returns iterator over the posts of requested blog page """
        if num < 1 or num > self.page_count:
            raise ValueError(
                'Page num should be within the range 1..%s' % self.page_count
            )
        offset = (num - 1) * self.page_len
        query = self._base_query()
        query = query \
            .order_by(models.Post.published.desc()) \
            .offset(offset) \
            .limit(self.page_len)
        return (self.get(str(post.id), post) for post in query.all())

    @reify
    def page_count(self):
        """ Returns number of pages in the blog """
        return int(math.ceil(float(self.post_count) / self.page_len))

    @reify
    def post_count(self):
        """ Returns number of posts in the blog """
        return self._base_query().count()

    def _base_query(self):
        """ Constructs base query """
        session = models.DBSession()
        query = session.query(models.Post)
        author = self.parent(cls=Author)
        if author:
            # If there is an Author resource in lineage,
            # query will return only author's posts.
            query = query.filter(models.Post.author == author.id)
        return query


@Blog.mount_set(DEC_ID)
class Post(Resource):
    """ Blog post resource """

    __not_exist__ = models.NoResultFound

    def on_init(self, post):
        """ Load blog post from database if it has not been loaded """
        if post is None:
            session = models.DBSession()
            query = session \
                .query(models.Post) \
                .filter(models.Post.id == int(self.__name__))
            author = self.parent(cls=Author)
            if author:
                query = query.filter(models.Post.author == author.id)
            post = query.one()
        self.id = post.id
        self.title = post.title
        self.published = post.published
        self.body = post.body
        self.author = post.author
