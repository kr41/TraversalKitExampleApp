import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'TraversalKit',
    'Markdown',
    'pyyaml',
]

setup(
    name='TraversalKitExampleApp',
    version='0.0',
    description='TraversalKit example application',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Dmitry Vakhrushev',
    author_email='self@kr41.net',
    license='WTFPL',
    url='https://bitbucket.org/kr41/traversalkitexampleapp',
    keywords='web wsgi bfg pylons pyramid traversal traversalkit',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='traversalkitexampleapp',
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = traversalkitexampleapp:main
    """,
)
