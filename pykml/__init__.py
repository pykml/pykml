import os
from lxml import etree

module_dir = os.path.split(__file__)[0]   # get the module path

schema_file_ogc = os.path.join(module_dir, "schemas", "ogckml22.xsd")
with open(schema_file_ogc) as f:
    schema_ogc = etree.XMLSchema(file=f)

schema_file_gx = os.path.join(module_dir, "schemas", "kml22gx.xsd")
with open(schema_file_gx) as f:
    schema_gx = etree.XMLSchema(file=f)