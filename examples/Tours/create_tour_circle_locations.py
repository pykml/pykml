'''Generate a KML document of a tour based on rotating around locations.

'''
from lxml import etree
from pykml.kml_gx import schema
from pykml.kml_gx.parser import parse
from pykml.kml_gx.factory import KML_ElementMaker as kml
from pykml.kml_gx.factory import GX_ElementMaker as gx

GX_ns = "{http://www.google.com/kml/ext/2.2}"

feature_list = [
    {
        'name':"Half Dome",
        'desc':'Northern Territory, central Australia',
        'lon':-119.53417,'lat':37.744728, 'tilt':45, 'range':3000,
    },
    {
        'name':"Ayers Rock",
        'desc':'Northern Territory, central Australia',
        'lon':131.035,'lat':-25.345, 'tilt':88, 'range':5000,
    },
    {
        'name':"Barbs Fabulous Faults for Mapping",
        'desc':'??',
        'lon':56.884102, 'lat':32.193918, 'tilt':30, 'range':10000,
    },
    {
        'name':"Chris Crosbys Earthquake Faults ",
        'desc':'Mexicali',
        'lon':-115.57914, 'lat':32.459667, 'tilt':30, 'range':50000,
    },
    {
        'name':"Landscape Arch",
        'desc':'Arches National Park, Utah, USA',
        'lon':-109.607,'lat':38.791, 'tilt':60, 'range':500,
    },
    {
        'name':"Manicouagan Crater",
        'desc':'Quebec, Canada',
        'lon':-68.7, 'lat':51.38, 'tilt':45, 'range':100000,
    },
#    {
#        'name':"Tylers PhD Plumbing Project",
#        'desc':'Niwot Ridge, Colorado, USA',
#        'lon':-105.57102, 'lat':40.047817, 'tilt':30, 'range':300,
#    },
    {
        'name':"Upheaval Dome",
        'desc':'Canyonlands National Park, Utah, USA',
        'lon':-109.929, 'lat':38.437, 'tilt':60, 'range':4000,
    },
    {
        'name':"Racetrack Playa",
        'desc':'Death Valley, California, USA',
        'lon':-117.56, 'lat':36.679, 'tilt':45, 'range':8000
    },
    {
        'name':"Matterhorn",
        'desc':'Pennine Alps, Switzerland/Italy',
        'lon':7.6584, 'lat':45.9766, 'tilt':60, 'range':6000,
    },
]
# start with a base KML tour and playlist
tour_doc = kml.kml(
    kml.Document(
      gx.Tour(
        kml.name("Play me!"),
        gx.Playlist(),
      ),
      kml.Folder(
        kml.name('Features'),
        id='features',
      ),
    )
)
for feature in feature_list:
    # fly to a space viewpoint
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
      gx.FlyTo(
        gx.duration(5),
        gx.flyToMode("smooth"),
        kml.LookAt(
          kml.longitude(feature['lon']),
          kml.latitude(feature['lat']),
          kml.altitude(0),
          kml.heading(0),
          kml.tilt(0),
          kml.range(10000000.0),
          kml.altitudeMode("relativeToGround"),
        )
      ),
    )
    # fly to the feature
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
      gx.FlyTo(
        gx.duration(5),
        gx.flyToMode("bounce"),
        kml.LookAt(
          kml.longitude(feature['lon']),
          kml.latitude(feature['lat']),
          kml.altitude(0),
          kml.heading(0),
          kml.tilt(feature['tilt']),
          kml.range(feature['range']),
          kml.altitudeMode("relativeToGround"),
        )
      ),
    )
    # spin around the feature
    for aspect in range(0,360,10):
        tour_doc.Document[GX_ns+"Tour"].Playlist.append(
          gx.FlyTo(
            gx.duration(0.25),
            gx.flyToMode("smooth"),
            kml.LookAt(
              kml.longitude(feature['lon']),
              kml.latitude(feature['lat']),
              kml.altitude(0),
              kml.heading(aspect),
              kml.tilt(feature['tilt']),
              kml.range(feature['range']),
              kml.altitudeMode("relativeToGround"),
            )
          )
        )
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(gx.Wait(gx.duration(1.0)))
    
#    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
#        gx.TourControl(gx.playMode("pause"))
#    )
    
    # add a placemark for the feature
    tour_doc.Document.Folder.append(
      kml.Placemark(
        kml.name("?"),
        kml.description(
            "<h1>{name}</h1><br/>{desc}".format(
                    name=feature['name'],
                    desc=feature['desc'],
            )
        ),
        kml.Point(
          kml.extrude(1),
          kml.altitudeMode("relativeToGround"),
          kml.coordinates("{lon},{lat},{alt}".format(
                  lon=feature['lon'],
                  lat=feature['lat'],
                  alt=50,
              )
          )
        ),
        id=feature['name'].replace(' ','_')
      )
    )
    # show the placemark balloon
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
        gx.AnimatedUpdate(
          gx.duration(2.0),
          kml.Update(
            kml.targetHref(),
            kml.Change(
              kml.Placemark(
                kml.visibility(1),
                gx.balloonVisibility(1),
                targetId=feature['name'].replace(' ','_')
              )
            )
          )
        )
    )
    
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(gx.Wait(gx.duration(2.0)))
    
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
        gx.AnimatedUpdate(
          gx.duration(2.0),
          kml.Update(
            kml.targetHref(),
            kml.Change(
              kml.Placemark(
                gx.balloonVisibility(0),
                targetId=feature['name'].replace(' ','_')
              )
            )
          )
        )
    )
    # fly to a space viewpoint
    tour_doc.Document[GX_ns+"Tour"].Playlist.append(
      gx.FlyTo(
        gx.duration(5),
        gx.flyToMode("bounce"),
        kml.LookAt(
          kml.longitude(feature['lon']),
          kml.latitude(feature['lat']),
          kml.altitude(0),
          kml.heading(0),
          kml.tilt(0),
          kml.range(10000000.0),
          kml.altitudeMode("relativeToGround"),
        )
      ),
    )

print etree.tostring(tour_doc, pretty_print=True)
schema.assertValid(tour_doc)
