import unittest
from os import path
from pykml.parser import Schema
from pykml.parser import parse
from pykml.factory import KML_ElementMaker as KML

class KmlUtilTestCase(unittest.TestCase):
    
    def test_count_elements(self):
        """Tests the counting of elements in a KML document."""
        from pykml.util import count_elements
        
        test_datafile = path.join(
            path.dirname(__file__),
            'testfiles',
            'google_kml_developers_guide/complete_tour_example.kml'
        )
        with open(test_datafile) as f:
            doc = parse(f, schema=Schema('kml22gx.xsd'))
        summary = count_elements(doc)
        
        self.assertTrue(summary.has_key('http://www.opengis.net/kml/2.2'))
        self.assertEqual(4,
            summary['http://www.opengis.net/kml/2.2']['Placemark']
        )
        self.assertTrue(summary.has_key('http://www.google.com/kml/ext/2.2'))
        self.assertEqual(5,
            summary['http://www.google.com/kml/ext/2.2']['FlyTo']
        )
        self.assertEqual(2,
            summary['http://www.google.com/kml/ext/2.2']['Wait']
        )
    
    def test_wrap_angle180(self):
        """Tests the wrap_angle180 utility function."""
        from pykml.util import wrap_angle180
        
        self.assertEqual(wrap_angle180(0), 0)
        self.assertEqual(wrap_angle180(180), -180)
        self.assertEqual(wrap_angle180(361), 1)
        # test passing an array
        self.assertEqual(wrap_angle180([0,180,361,]), [0,-180,1,])

    def test_to_wkt_list_simple_polygon(self):
        """Tests the to_wkt_list function for a polygon with inner rings."""
        from pykml.util import to_wkt_list
        
        # create a polygon
        poly = KML.Polygon(
            KML.extrude('1'),
            KML.altitudeMode('relativeToGround'),
            KML.outerBoundaryIs(
              KML.LinearRing(
                KML.coordinates(
                '-122.366278,37.818844,30 '
                '-122.365248,37.819267,30 '
                '-122.365640,37.819861,30 '
                '-122.366669,37.819429,30 '
                '-122.366278,37.818844,30 '
                ),
              ),
            ),
          )
        
        poly_wkt_list = to_wkt_list(poly)
        
        self.assertEqual(len(poly_wkt_list), 1)
        self.assertEqual(
            poly_wkt_list[0], 
            ('POLYGON ((-122.366278 37.818844 30, '
                       '-122.365248 37.819267 30, '
                       '-122.365640 37.819861 30, '
                       '-122.366669 37.819429 30, '
                       '-122.366278 37.818844 30))')
        )

    
    def test_to_wkt_list_complex_polygon(self):
        """Tests the to_wkt_list function for a polygon with inner rings."""
        from pykml.util import to_wkt_list
        
        # create a polygon
        poly = KML.Polygon(
            KML.extrude('1'),
            KML.altitudeMode('relativeToGround'),
            KML.outerBoundaryIs(
              KML.LinearRing(
                KML.coordinates(
                '-122.366278,37.818844,30 '
                '-122.365248,37.819267,30 '
                '-122.365640,37.819861,30 '
                '-122.366669,37.819429,30 '
                '-122.366278,37.818844,30 '
                ),
              ),
            ),
            KML.innerBoundaryIs(
              KML.LinearRing(
                KML.coordinates(
                '-122.366212,37.818977,30 '
                '-122.365424,37.819294,30 '
                '-122.365704,37.819731,30 '
                '-122.366212,37.818977,30 '
                ),
              ),
            ),
            KML.innerBoundaryIs(
              KML.LinearRing(
                KML.coordinates(
                '-122.366212,37.818977,30 '
                '-122.365704,37.819731,30 '
                '-122.366488,37.819402,30 '
                '-122.366212,37.818977,30 '
                ),
              ),
            ),
          )
        
        poly_wkt_list = to_wkt_list(poly)
        
        self.assertEqual(len(poly_wkt_list), 1)
        self.assertEqual(
            poly_wkt_list[0], 
            ('POLYGON ((-122.366278 37.818844 30, '
                       '-122.365248 37.819267 30, '
                       '-122.365640 37.819861 30, '
                       '-122.366669 37.819429 30, '
                       '-122.366278 37.818844 30), '
                      '(-122.366212 37.818977 30, '
                       '-122.365424 37.819294 30, '
                       '-122.365704 37.819731 30, '
                       '-122.366212 37.818977 30), '
                      '(-122.366212 37.818977 30, '
                       '-122.365704 37.819731 30, '
                       '-122.366488 37.819402 30, '
                       '-122.366212 37.818977 30))')
        )