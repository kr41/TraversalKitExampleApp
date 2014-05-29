from pyramid.config import Configurator

from . import resources
from . import models


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application """
    models.configure(settings)
    models.initialize()
    # It's bad idea to create database and load fixtures during application
    # start.  However it's OK for quick start in educational application.
    # Just don't do that in your production ones.
    config = Configurator(
        settings=settings,
        root_factory=resources.root_factory
    )
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
