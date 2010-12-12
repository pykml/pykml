import unittest
import urllib2
from lxml import etree
from StringIO import StringIO

from pykml.kml_ogc.parser import fromstring
from pykml.kml_ogc.parser import parse

class ParseTestCase(unittest.TestCase):
    "A collection of tests related to parsing KML documents"
    
    def test_fromstring_kml_document(self):
        "Tests the parsing of an valid KML string"
        test_kml = '<kml xmlns="http://www.opengis.net/kml/2.2"/>'
        tree = fromstring(test_kml, validate=True)
        self.assertEquals(etree.tostring(tree), test_kml)
        tree = fromstring(test_kml, validate=False)
        self.assertEquals(etree.tostring(tree), test_kml)
    
    def test_fromstring_invalid_kml_document(self):
        "Tests the parsing of an invalid KML string"
        test_kml = '<bad_element />'
        try:
            tree = fromstring(test_kml, validate=True)
            self.assertTrue(False)
        except etree.XMLSyntaxError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def test_parse_kml_document(self):
        "Tests the parsing of an valid KML file object"
        test_kml = '<kml xmlns="http://www.opengis.net/kml/2.2"/>'
        fileobject = StringIO(test_kml)
        tree = parse(fileobject, validate=True)
        self.assertEquals(etree.tostring(tree), test_kml)
        tree = parse(fileobject, validate=False)
        self.assertEquals(etree.tostring(tree), test_kml)
    
    def test_parse_invalid_kml_document(self):
        "Tests the parsing of an invalid KML document"
        fileobject = StringIO('<bad_element />')
        try:
            tree = parse(fileobject, validate=True)
            self.assertTrue(False)
        except etree.XMLSyntaxError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def test_parse_kml_url(self):
        "Tests the parsing of a KML URL"
        url = 'http://code.google.com/apis/kml/documentation/KML_Samples.kml'
        #url = 'http://kml-samples.googlecode.com/svn/trunk/kml/Document/doc-with-id.kml'
        #url = 'http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml'
        #url = 'http://code.google.com/apis/kml/documentation/kmlfiles/animatedupdate_example.kml'
        fileobject = urllib2.urlopen(url)
        tree = parse(fileobject, validate=True)
        self.assertEquals(
            etree.tostring(tree)[:78],
            '<kml xmlns="http://www.opengis.net/kml/2.2">'
              '<Document>'
                '<name>KML Samples</name>'
        )
    
    def test_parse_invalid_ogc_kml_document(self):
        """Tests the parsing of an invalid KML document.  Note that this KML
        document uses elements that are not in the OGC KML spec.
        """
        url = 'http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml'
        fileobject = urllib2.urlopen(url)
        try:
            tree = parse(fileobject, validate=True)
            self.assertTrue(False)
        except etree.XMLSyntaxError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()