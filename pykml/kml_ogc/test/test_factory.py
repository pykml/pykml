import unittest
from lxml import etree

from pykml.kml_ogc import schema
from pykml.kml_ogc.factory import KML_ElementMaker as K
from pykml.kml_ogc.factory import ATOM_ElementMaker as ATOM

class KmlFactoryTestCase(unittest.TestCase):
    
    def test_trivial_kml_document(self):
        """Tests the creation of a trivial OGC KML document."""
        doc = K.kml()
        self.assertTrue(schema.validate(doc))
        self.assertEquals(
            etree.tostring(doc),
            '<kml xmlns:atom="http://www.w3.org/2005/Atom" '
                 'xmlns="http://www.opengis.net/kml/2.2"/>'
        )
    
    def test_basic_kml_document(self):
        """Tests the creation of a basic OGC KML document."""
        doc = K.kml(
            K.Document(
                K.name("KmlFile"),
                K.Placemark(
                    K.name("Untitled Placemark"),
                    K.Point(
                        K.coordinates("-95.265,38.959,0")
                    )
                )
            )
        )
        self.assertTrue(schema.validate(doc))
        self.assertEquals(
            etree.tostring(doc),
            '<kml xmlns:atom="http://www.w3.org/2005/Atom" '
                 'xmlns="http://www.opengis.net/kml/2.2">'
              '<Document>'
                '<name>KmlFile</name>'
                '<Placemark>'
                  '<name>Untitled Placemark</name>'
                  '<Point>'
                    '<coordinates>-95.265,38.959,0</coordinates>'
                  '</Point>'
                '</Placemark>'
              '</Document>'
            '</kml>'
        )
    
    def test_kml_document_with_atom_element(self):
        """Tests the creation of a KML document with an ATOM element."""
        doc = K.kml(
            K.Document(
                ATOM.author(
                    ATOM.name("J. K. Rowling")
                ),
                ATOM.link(href="http://www.harrypotter.com"),
                K.Placemark(
                    K.name("Hogwarts"),
                    K.Point(
                        K.coordinates("1,1")
                    )
                )
            )
        )
        self.assertTrue(schema.validate(doc))
        self.assertEquals(
            etree.tostring(doc),
            '<kml xmlns:atom="http://www.w3.org/2005/Atom" '
                 'xmlns="http://www.opengis.net/kml/2.2">'
              '<Document>'
                '<atom:author>'
                  '<atom:name>J. K. Rowling</atom:name>'
                '</atom:author>'
                '<atom:link href="http://www.harrypotter.com"/>'
                '<Placemark>'
                  '<name>Hogwarts</name>'
                  '<Point>'
                    '<coordinates>1,1</coordinates>'
                  '</Point>'
                '</Placemark>'
              '</Document>'
            '</kml>'
        )

