'''
Create LXML ElementMaker objects that create KML objects using the 
appropriate namespace
'''

from lxml import objectify

# create a factory object for creating objects in the KML namespace
KML_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.opengis.net/kml/2.2",
    nsmap={
        None: "http://www.opengis.net/kml/2.2",
        #'kml': "http://www.opengis.net/kml/2.2",
        'atom': "http://www.w3.org/2005/Atom",
    }
)

# create a factory object for creating objects in the ATOM namespace
ATOM_ElementMaker = objectify.ElementMaker(
    annotate=False,
    namespace="http://www.w3.org/2005/Atom",
    nsmap={'atom': "http://www.w3.org/2005/Atom"}
)
