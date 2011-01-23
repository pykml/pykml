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

class GeneratePythonScriptTestCase(unittest.TestCase):
    
    def test_write_python_script_for_kml_document(self):
        """Tests the creation of a trivial OGC KML document."""
        from pykml.kml_ogc.factory import write_python_script_for_kml_document
        
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
        script = write_python_script_for_kml_document(doc)
        self.assertEquals(
            script,
            'from pykml.kml_gx.factory import KML_ElementMaker as KML\n'
            'from pykml.kml_gx.factory import ATOM_ElementMaker as ATOM\n'
            'from pykml.kml_gx.factory import GX_ElementMaker as GX\n'
            '\n'
            'doc = KML.kml(\n'
            '  KML.Document(\n'
            '    ATOM.author(\n'
            '      ATOM.name("J. K. Rowling"),\n'
            '    ),\n'
            '    ATOM.link(href="http://www.harrypotter.com",),\n'
            '    KML.Placemark(\n'
            '      KML.name("Hogwarts"),\n'
            '      KML.Point(\n'
            '        KML.coordinates("1,1"),\n'
            '      ),\n'
            '    ),\n'
            '  ),\n'
            ')\n'
            '\n'
            'from lxml import etree\n'
            'print etree.tostring(doc,pretty_print=True)\n'
        )

    def test_write_python_script_for_kml_document_with_cdata(self):
        """Tests the creation of an OGC KML document with a cdata tag"""

    """
    <Style id="noDrivingDirections">
      <BalloonStyle>
        <text><![CDATA[
          <b>$[name]</b>
          <br /><br />
          $[description]
        ]]></text>
      </BalloonStyle>
    </Style>
    """
    pass

if __name__ == '__main__':
    unittest.main()