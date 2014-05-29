import os
import yaml

from sqlalchemy import engine_from_config
from sqlalchemy import Column, Integer, Unicode, Text, DateTime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


def configure(settings):
    """ Configure database """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine


def initialize():
    """ Create database and load fixtures """
    Base.metadata.create_all()
    here = os.path.abspath(os.path.dirname(__file__))
    fixtures = os.path.join(here, 'fixtures')
    for filename in os.listdir(fixtures):
        table = os.path.splitext(filename)[0]
        table = Base.metadata.tables[table]
        insert = table.insert()
        try:
            with Base.metadata.bind.begin() as conn:
                with open(os.path.join(fixtures, filename)) as f:
                    for item in yaml.load(f):
                        conn.execute(insert, **item)
        except IntegrityError:
            # Fixtures have been already loaded
            pass


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255))
    published = Column(DateTime)
    body = Column(Text)
    author = Column(Integer)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255))
    name = Column(Unicode(255))
    about = Column(Text)
