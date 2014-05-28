import math

from pyramid.decorator import reify
from traversalkit import Resource, DEC_ID, TEXT_ID

from . import models


def root_factory(request):
    return SiteRoot()


class SiteRoot(Resource):

    title = 'TraversalKit Example Application'


@SiteRoot.mount('authors')
class Authors(Resource):

    title = 'Authors'

    def all(self):
        session = models.DBSession()
        query = session.query(models.Author)
        for author in query.all():
            yield self.child(Author, author.username, author)


@Authors.mount_set(TEXT_ID)
class Author(Resource):

    __not_exist__ = models.NoResultFound

    def on_init(self, author):
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

    page_len = 5

    @reify
    def title(self):
        return 'Articles' if self.parent(cls=Author) else 'Blog'

    def page(self, num):
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
        for post in query.all():
            yield self.child(Post, str(post.id), post)

    @reify
    def page_count(self):
        return int(math.ceil(float(self.post_count) / self.page_len))

    @reify
    def post_count(self):
        return self._base_query().count()

    def _base_query(self):
        session = models.DBSession()
        query = session.query(models.Post)
        author = self.parent(cls=Author)
        if author:
            query = query.filter(models.Post.author == author.id)
        return query



@Blog.mount_set(DEC_ID)
class Post(Resource):

    __not_exist__ = models.NoResultFound

    def on_init(self, post):
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
