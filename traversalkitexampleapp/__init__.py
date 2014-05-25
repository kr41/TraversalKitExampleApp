from pyramid.config import Configurator

from . import resources
from . import models


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application """
    models.configure(settings)
    models.initialize()
    config = Configurator(
        settings=settings,
        root_factory=resources.root_factory
    )
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
