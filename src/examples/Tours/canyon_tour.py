'''Generate a KML document of a tour through the grand canyon.

'''

from lxml import etree
from pykml.kml_gx import schema
from pykml.kml_gx.factory import KML_ElementMaker as kml
from pykml.kml_gx.factory import GX_ElementMaker as gx

doc = kml.kml(
    gx.Tour(
      kml.name("Play me!"),
      gx.Playlist(
        gx.FlyTo(
          gx.duration(5.0),
          kml.LookAt(
            kml.longitude(-111.5878),
            kml.latitude(36.8650),
            kml.altitude(0),
            kml.heading(-129.7),
            kml.tilt(73.0),
            kml.range(300),
            kml.altitudeMode("relativeToGround"),
          )
        ),
        gx.Wait(
          gx.duration(1.0)
        ),
        gx.FlyTo(
          gx.duration(6.0),
          kml.Camera(
            kml.longitude(174.063),
            kml.latitude(-39.663),
            kml.altitude(18275),
            kml.heading(-4.921),
            kml.tilt(65),
            kml.altitudeMode("absolute"),
          )
        ),
      )
    )
)
assert schema.validate(doc)
print etree.tostring(doc, pretty_print=True)
