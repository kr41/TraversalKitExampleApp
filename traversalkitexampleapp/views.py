from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from . import resources


@view_config(context=resources.SiteRoot, renderer='/siteroot/home.mako')
def home(context, request):
    """ Handles home page """
    return {}


@view_config(context=resources.Authors, renderer='/authors/index.mako')
def author_index(context, request):
    """ Handles list of authors """
    return {'authors': context.all()}


@view_config(context=resources.Author, renderer='/authors/author.mako')
def author(context, request):
    """ Handles author's profile """
    return {'author': context}


@view_config(context=resources.Blog, renderer='/blog/index.mako')
def blog_index(context, request):
    """ Handles blog index page """
    try:
        # Get posts of requested page. If page number is invalid integer,
        # or out of range, it will raise "404 Not Found".
        page_num = int(request.GET.get('page', 1))
        posts = list(context.page(page_num))
    except ValueError:
        raise HTTPNotFound()
    authors = {}
    if not context.parent(cls=resources.Author):
        # If Blog resource (context) has no Author one in its lineage,
        # then we need to render link to author's profile.  Therefore
        # we need to get author resources.
        ids = set(p.author for p in posts)
        print ids
        authors = dict((a.id, a) for a in request.root['authors'].all(ids))
    return {
        'posts': posts,
        'page_num': page_num,
        'page_count': context.page_count,
        'authors': authors,
    }


@view_config(context=resources.Post, renderer='/blog/post.mako')
def post(context, request):
    """ Handles blog post page """
    author = None
    if not context.parent(cls=resources.Author):
        author = request.root['authors'].by_id(context.author)
    return {
        'post': context,
        'author': author,
    }
