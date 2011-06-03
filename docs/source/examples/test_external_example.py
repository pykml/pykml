from pykml.factory import KML_ElementMaker as KML
from lxml import etree

pm1 = KML.Placemark(
                KML.name("Hello World!"),
                KML.Point(
                  KML.coordinates("-64.5253,18.4607")
                )
              )

etree.tostring(pm1)

