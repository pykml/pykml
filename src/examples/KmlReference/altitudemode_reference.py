'''Generate a KML string that matches the altitudemode example.

References:
http://code.google.com/apis/kml/documentation/kmlreference.html#gxaltitudemode
http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml
'''

from lxml import etree
from pykml.kml_gx import schema
from pykml.kml_gx.factory import KML_ElementMaker as K
from pykml.kml_gx.factory import GX_ElementMaker as GX

doc = K.kml(
    K.Placemark(
        K.name("gx:altitudeMode Example"),
        K.LookAt(
            K.longitude(146.806),
            K.latitude(12.219),
            K.heading(-60),
            K.tilt(70),
            K.range(6300),
            GX.altitudeMode("relativeToSeaFloor"),
        ),
        K.LineString(
            K.extrude(1),
            GX.altitudeMode("relativeToSeaFloor"),
            K.coordinates(
              "146.825,12.233,400 "
              "146.820,12.222,400 "
              "146.812,12.212,400 "
              "146.796,12.209,400 "
              "146.788,12.205,400"
            )
        )
    )
)

print etree.tostring(doc, pretty_print=True)
assert schema.validate(doc)
