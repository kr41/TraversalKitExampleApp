import math

from pyramid.decorator import reify
from traversalkit import Resource, DEC_ID

from . import models


def root_factory(request):
    return SiteRoot()


class SiteRoot(Resource):

    title = 'TraversalKit Example Application'


@SiteRoot.mount('blog')
class Blog(Resource):

    title = 'Blog'
    page_len = 5

    def page(self, num):
        if num < 1 or num > self.page_count:
            raise ValueError(
                'Page num should be within the range 1..%s' % self.page_count
            )
        offset = (num - 1) * self.page_len
        session = models.DBSession()
        query = session \
            .query(models.Post) \
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
        session = models.DBSession()
        return session.query(models.Post).count()


@Blog.mount_set(DEC_ID)
class Post(Resource):

    __not_exist__ = models.NoResultFound

    def on_init(self, post):
        if post is None:
            session = models.DBSession()
            query = session \
                .query(models.Post) \
                .filter(models.Post.id == int(self.__name__))
            post = query.one()
        self.id = post.id
        self.title = post.title
        self.published = post.published
        self.body = post.body
