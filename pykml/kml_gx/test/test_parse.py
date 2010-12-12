import unittest
import urllib2
from lxml import etree
from StringIO import StringIO

from pykml.kml_gx.parser import fromstring
from pykml.kml_gx.parser import parse

class ParseTestCase(unittest.TestCase):
    "A collection of tests related to parsing KML documents"
    
    def test_parse_kml_url(self):
        "Tests the parsing of a KML URL"
        url = 'http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml'
        fileobject = urllib2.urlopen(url)
        tree = parse(fileobject, validate=True)
        self.assertEquals(
            etree.tostring(tree)[:185],
            '<kml xmlns="http://www.opengis.net/kml/2.2" '
                 'xmlns:gx="http://www.google.com/kml/ext/2.2">'
                '<!-- required when using gx-prefixed elements -->'
                '<Placemark>'
                  '<name>gx:altitudeMode Example</name>'
        )

    def test_parse_kml_url_2(self):
        "Tests the parsing of a KML URL"
        url = 'http://code.google.com/apis/kml/documentation/kmlfiles/animatedupdate_example.kml'
        fileobject = urllib2.urlopen(url)
        tree = parse(fileobject, validate=True)
        #import ipdb; ipdb.set_trace()
        self.assertEquals(
            etree.tostring(tree)[:137],
            '<kml xmlns="http://www.opengis.net/kml/2.2" '
                 'xmlns:gx="http://www.google.com/kml/ext/2.2">'
                '<Document>'
                  '<name>gx:AnimatedUpdate example</name>'
        )

if __name__ == '__main__':
    unittest.main()