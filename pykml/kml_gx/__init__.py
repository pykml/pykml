import os
from lxml import etree

module_dir = os.path.split(__file__)[0]   # get the module path
schema_file = os.path.join(module_dir, "schemas", "kml22gx.xsd")
with open(schema_file) as f:
    schema = etree.XMLSchema(file=f)
