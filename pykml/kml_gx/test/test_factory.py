import unittest
from lxml import etree

from pykml.kml_gx import schema
from pykml.kml_gx.factory import KML_ElementMaker as K
from pykml.kml_gx.factory import ATOM_ElementMaker as ATOM
from pykml.kml_gx.factory import GX_ElementMaker as GX

class KmlFactoryTestCase(unittest.TestCase):
    """Class that tests the generation of KML using factory objects"""
    
    def test_basic_kml_document(self):
        """Tests the creation of a basic KML with Google Extensions ."""
        doc = K.kml(
            GX.Tour(
                GX.Playlist(
                    GX.SoundCue(
                        K.href("http://dev.keyhole.com/codesite/cntowerfacts.mp3")
                    ),
                    GX.Wait(
                        GX.duration(10)
                    ),
                    GX.FlyTo(
                        GX.duration(5),
                        GX.flyToMode("bounce"),
                        K.LookAt(
                            K.longitude(-79.387),
                            K.latitude(43.643),
                            K.altitude(0),
                            K.heading(-172.3),
                            K.tilt(10),
                            K.range(1200),
                            K.altitudeMode("relativeToGround"),
                        )
                    )
                )
            )
        )
        self.assertTrue(schema.validate(doc))
        self.assertEquals(
            etree.tostring(doc),
            '<kml xmlns:gx="http://www.google.com/kml/ext/2.2" '
                 'xmlns:atom="http://www.w3.org/2005/Atom" '
                 'xmlns="http://www.opengis.net/kml/2.2">'
              '<gx:Tour>'
                '<gx:Playlist>'
                  '<gx:SoundCue>'
                    '<href>http://dev.keyhole.com/codesite/cntowerfacts.mp3</href>'
                  '</gx:SoundCue>'
                  '<gx:Wait>'
                    '<gx:duration>10</gx:duration>'
                  '</gx:Wait>'
                  '<gx:FlyTo>'
                    '<gx:duration>5</gx:duration>'
                    '<gx:flyToMode>bounce</gx:flyToMode>'
                    '<LookAt>'
                      '<longitude>-79.387</longitude>'
                      '<latitude>43.643</latitude>'
                      '<altitude>0</altitude>'
                      '<heading>-172.3</heading>'
                      '<tilt>10</tilt>'
                      '<range>1200</range>'
                      '<altitudeMode>relativeToGround</altitudeMode>'
                    '</LookAt>'
                  '</gx:FlyTo>'
                '</gx:Playlist>'
              '</gx:Tour>'
            '</kml>'
        )

