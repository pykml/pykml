'''Generate a KML string that matches the animated update example.

References:
http://code.google.com/apis/kml/documentation/kmlreference.html#gxanimatedupdate
http://code.google.com/apis/kml/documentation/kmlfiles/animatedupdate_example.kml

Note that as of 12/1/2010, the KML code displayed beneath the animatedupdate_example.kml link
is not valid.
* The <scale> element should not be a subelement of <Icon>.
* The <gx:duration> element should be the first subelement of <gx:FlyTo>
'''

from lxml import etree
from pykml.kml_gx import schema
from pykml.kml_gx.factory import KML_ElementMaker as K
from pykml.kml_gx.factory import GX_ElementMaker as GX

doc = K.kml(
  K.Document(
    K.name("gx:AnimatedUpdate example"),
    K.Style(
      K.IconStyle(
        K.scale(1.0),
        K.Icon(
          K.href("http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png"),
        ),
        id="mystyle"
      ),
      id="pushpin"
    ),
    K.Placemark(
      K.name("Pin on a mountaintop"),
      K.styleUrl("#pushpin"),
      K.Point(
        K.coordinates(170.1435558771009,-43.60505741890396,0)
      ),
      id="mountainpin1"
    ),
    GX.Tour(
      K.name("Play me!"),
      GX.Playlist(
        GX.FlyTo(
          GX.duration(3),
          GX.flyToMode("bounce"),
          K.Camera(
            K.longitude(170.157),
            K.latitude(-43.671),
            K.altitude(9700),
            K.heading(-6.333),
            K.tilt(33.5),
          )
        ),
        GX.AnimatedUpdate(
          GX.duration(5),
          K.Update(
            K.targetHref(),
            K.Change(
              K.IconStyle(
                K.scale(10.0),
                targetId="mystyle"
              )
            )
          )
        ),
        GX.Wait(
          GX.duration(5)
        )
      )
    )
  )
)

print etree.tostring(doc, pretty_print=True)
schema.assertValid(doc)
