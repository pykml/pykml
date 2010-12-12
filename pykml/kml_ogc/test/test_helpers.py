import unittest
#from lxml import etree

#from pykml.kml_ogc import schema
#from pykml.kml_ogc.factory import KML_ElementMaker as K
#from pykml.kml_ogc.factory import ATOM_ElementMaker as ATOM

from pykml.kml_ogc.parser import fromstring

class KmlHelpersTestCase(unittest.TestCase):
    
    def test_trivial_kml_document(self):
        """Tests the creation of a trivial OGC KML document."""
        
        from pykml.kml_ogc.helpers import set_max_decimal_places
        
        test_kml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<kml xmlns="http://www.opengis.net/kml/2.2" '
                 'xmlns:gx="http://www.google.com/kml/ext/2.2" '
                 'xmlns:kml="http://www.opengis.net/kml/2.2" '
                 'xmlns:atom="http://www.w3.org/2005/Atom">'
                '<Document>'
                    '<Placemark>'
                        '<name>Spearhead</name>'
                        '<LookAt>'
                            '<longitude>-105.6381333137406</longitude>'
                            '<latitude>40.25542364754504</latitude>'
                            '<altitude>0</altitude>'
                            '<heading>-75.2679217880259</heading>'
                            '<tilt>23.33768008163944</tilt>'
                            '<range>236.1426918505284</range>'
                            '<altitudeMode>relativeToGround</altitudeMode>'
                        '</LookAt>'
                        '<Point>'
                            '<altitudeMode>absolute</altitudeMode>'
                            '<coordinates>-105.6381333137406,40.25542364754504,3826.997917950211</coordinates>'
                        '</Point>'
                    '</Placemark>'
                '</Document>'
                '</kml>'
        )
        doc = fromstring(test_kml, validate=True)
        set_max_decimal_places(doc, max_decimals=4)
        
        # test that the number of decimal places is four
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}longitude"),
            -105.6381
        )
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}latitude"),
            40.2554
        )
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}altitude"),
            0
        )
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}heading"),
            -75.2679
        )
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}tilt"),
            23.3377
        )
        self.assertAlmostEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}range"),
            236.1427
        )
        #import ipdb; ipdb.set_trace()
        self.assertEquals(
            doc.find(".//{http://www.opengis.net/kml/2.2}coordinates"),
            "-105.6381,40.2554,3826.9979"
        )