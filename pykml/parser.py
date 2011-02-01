'''
Parse KML file objects
'''
import os
from lxml import etree, objectify
#from __init__ import schema

class Schema():
    "Validate documents via an XML Schema"
    def __init__(self, schema):
        module_dir = os.path.split(__file__)[0]   # get the module path
        schema_file = os.path.join(module_dir, "schemas", schema)
        with open(schema_file) as f:
            self.schema = etree.XMLSchema(file=f)
    
    def schema(self):
        return self.schema
    
#    def __call__(self):
#        import ipdb; ipdb.set_trace()
#        return self.schema


def fromstring(text, schema=None):
    "Parses a file object using the KML OGC schema"
    if schema:
        parser = objectify.makeparser(schema = schema.schema)
        return objectify.fromstring(text, parser=parser)
    else:
        return objectify.fromstring(text)

def parse(fileobject, schema=None):
    """Parses a file object, and optionally validates it against the
    OGC KML Schema
    """
    if schema:
        # with validation
        parser = objectify.makeparser(schema = schema.schema)
        return objectify.parse(fileobject, parser=parser)
    else:
        # without validation
        return objectify.parse(fileobject)
