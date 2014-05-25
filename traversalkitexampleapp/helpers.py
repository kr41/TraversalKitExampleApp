from markupsafe import Markup as _markup
from markdown import markdown as _markdown


def markdown(text):
    return _markup(_markdown(text))
