'''
Parse KML file objects
'''

from lxml import objectify
from __init__ import schema

def fromstring(text, validate=True):
    "Parses a file object using the KML OGC schema"
    if validate:
        parser = objectify.makeparser(schema = schema)
        return objectify.fromstring(text, parser=parser)
    else:
        return objectify.fromstring(text)

def parse(fileobject, validate=True):
    """Parses a file object, and optionally validates it against the
    OGC KML Schema
    """
    if validate:
        # with validation
        parser = objectify.makeparser(schema = schema)
        #import ipdb; ipdb.set_trace()
        return objectify.parse(fileobject, parser=parser)
    else:
        # without validation
        return objectify.parse(fileobject)
