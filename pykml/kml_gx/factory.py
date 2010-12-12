from ..kml_ogc.factory import *

# Create a factory object for creating objects in the KML namespace
# This overwrites the OGC KML factory object and adds the 'gx' namespace
KML_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.opengis.net/kml/2.2",
    nsmap={
        None: "http://www.opengis.net/kml/2.2",
        'atom': "http://www.w3.org/2005/Atom",
        'gx': "http://www.google.com/kml/ext/2.2",
    }
)

# Create a factory object for creating objects in the KML Google Extension
# namespace
GX_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.google.com/kml/ext/2.2",
    nsmap={'gx': "http://www.google.com/kml/ext/2.2"}
)
