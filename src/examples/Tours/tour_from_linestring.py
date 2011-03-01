'''Generate a KML document of a tour based on a KML linestring.

'''
from lxml import etree
from pykml.kml_gx import schema
from pykml.kml_gx.parser import parse
from pykml.kml_gx.factory import KML_ElementMaker as kml
from pykml.kml_gx.factory import GX_ElementMaker as gx

GX_ns = "{http://www.google.com/kml/ext/2.2}"

# start with a base KML tour and playlist
tour_doc = kml.kml(
    gx.Tour(
      kml.name("Play me!"),
      gx.Playlist(),
    )
)

with open("examples/Tours/colorado_river_linestring.kml") as f:
    linestring_doc = parse(f)

# get the coordinate string of the first KML coordinate element
coord_str = str(
    linestring_doc.find(".//{http://www.opengis.net/kml/2.2}coordinates")
).strip()

#import ipdb; ipdb.set_trace()
#pass

for vertex in coord_str.split(' '):
    (lon,lat,alt) = vertex.split(',')
    flyto = gx.FlyTo(
        gx.duration(2),
        gx.flyToMode("smooth"),
        kml.Camera(
          kml.longitude(lon),
          kml.latitude(lat),
          kml.altitude(0),
          kml.heading(-129.7),
          kml.tilt(90.0),
          kml.altitudeMode("relativeToGround"),
        )
    )
    tour_doc[GX_ns+"Tour"].Playlist.append(flyto)

assert schema.validate(tour_doc)
print etree.tostring(tour_doc, pretty_print=True)

