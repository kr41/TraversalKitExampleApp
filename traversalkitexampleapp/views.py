from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from . import resources


@view_config(context=resources.SiteRoot, renderer='/siteroot/home.mako')
def home(context, request):
    return {}


@view_config(context=resources.Authors, renderer='/authors/index.mako')
def author_index(context, request):
    return {'authors': context.all()}


@view_config(context=resources.Author, renderer='/authors/author.mako')
def author(context, request):
    return {'author': context}


@view_config(context=resources.Blog, renderer='/blog/index.mako')
def blog_index(context, request):
    try:
        page_num = int(request.GET.get('page', 1))
        posts = list(context.page(page_num))
    except ValueError:
        raise HTTPNotFound()
    return {
        'posts': posts,
        'page_num': page_num,
        'page_count': context.page_count,
    }


@view_config(context=resources.Post, renderer='/blog/post.mako')
def post(context, request):
    return {'post': context}
