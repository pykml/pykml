from ..kml_ogc.helpers import *

def uses_google_extensions(doc):
    "Returns true if the KML document uses Google Extension elements"
    return 'gx' in get_namespaces_utilized(doc)

