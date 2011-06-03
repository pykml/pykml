'''
Parse KML file objects
'''
import os
from lxml import etree, objectify

class Schema():
    "Validate documents via an XML Schema"
    def __init__(self, schema):
        module_dir = os.path.split(__file__)[0]   # get the module path
        schema_file = os.path.join(module_dir, "schemas", schema)
        with open(schema_file) as f:
            self.schema = etree.XMLSchema(file=f)
    
    def validate(self, doc):
        "Checks if an XML document is valid (returns: boolean)"
        return self.schema.validate(doc)
    
    def assertValid(self, doc):
        """Checks if an XML document is valid (returns: None or an exception)
        
        The method generates a validation error if the document is not valid
        """
        return self.schema.assertValid(doc)

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
        parser = objectify.makeparser(schema = schema.schema, strip_cdata=False)
        return objectify.parse(fileobject, parser=parser)
    else:
        # without validation
        return objectify.parse(fileobject)
