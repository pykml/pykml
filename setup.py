from setuptools import setup, find_packages
import sys, os

version = '0.0.2'

setup(
    name='pykml',
    version=version,
    packages=[
        'pykml',
        'pykml.kml_ogc',
        'pykml.kml_gx',
    ],
    package_data={
        'pykml.kml_ogc': ['schemas/*.xsd', 'test/*.py'],
        'pykml.kml_gx': ['schemas/*.xsd', 'test/*.py'],
    },
    install_requires=[
        'setuptools',
        'lxml>=2.2.6',
    ],
    tests_require=['nose'],
    #test_suite='nose.collector',
    description="Python KML library",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='kml',
    author='Tyler Erickson',
    author_email='tylerickson@gmail.com',
    url='http://pypi.python.org/pypi/pykml',
    license='BSD',
    long_description="""\
=========
PyKML
=========
PyKML is a Python package for parsing and authoring KML documents. It is based
on the lxml.objectify API (http://codespeak.net/lxml/objectify.html) which
provides Pythonic access to XML documents.

------------
Dependencies
------------
* lxml

------------
Installation
------------
PyKML can be installed from the Python Package Index, using either easy_install
or pip:

  $ sudo easy_install pykml
  
or

  $ sudo pip install pykml

------
Usage
------

KML documents can be constructed by using element factory objects.  The
following example uses two factory objects, corresponding to the OGC KML and
ATOM namespaces:

  >>> from pykml.kml_ogc.factory import KML_ElementMaker as K
  >>> from pykml.kml_ogc.factory import ATOM_ElementMaker as ATOM
  >>> doc = K.kml(
  ...         K.Document(
  ...           ATOM.author(
  ...             ATOM.name("J. K. Rowling")
  ...           ),
  ...           ATOM.link(href="http://www.harrypotter.com"),
  ...           K.Placemark(
  ...             K.name("Hogwarts"),
  ...             K.Point(
  ...               K.coordinates("1,1")
  ...             )
  ...           )
  ...         )
  ...       )

Constructed documents can be converted to a string respresentation:

  >>> from lxml import etree
  >>> etree.tostring(doc)

and can be validated against the official KML XML Schema: 

  >>> from pykml.kml_ogc import schema
  >>> print schema.validate(doc)

Existing KML documents can also be parsed:

  >>> import urllib2
  >>> from pykml.kml_ogc.parser import parse
  >>> url = 'http://code.google.com/apis/kml/documentation/KML_Samples.kml'
  >>> fileobject = urllib2.urlopen(url)
  >>> tree = parse(fileobject, validate=True)

Documents that make use of the Google Extension namespace elements can be 
created by importing the appropriate factory objects:

  >>> from pykml.kml_gx import schema
  >>> from pykml.kml_gx.factory import KML_ElementMaker as K
  >>> from pykml.kml_gx.factory import ATOM_ElementMaker as ATOM
  >>> from pykml.kml_gx.factory import GX_ElementMaker as GX
  >>> doc = K.kml(
  ...       GX.Tour(
  ...         GX.Playlist(
  ...           GX.SoundCue(
  ...             K.href("http://dev.keyhole.com/codesite/cntowerfacts.mp3")
  ...           ),
  ...           GX.Wait(
  ...             GX.duration(10)
  ...           ),
  ...           GX.FlyTo(
  ...             GX.duration(5),
  ...             GX.flyToMode("bounce"),
  ...             K.LookAt(
  ...               K.longitude(-79.387),
  ...               K.latitude(43.643),
  ...               K.altitude(0),
  ...               K.heading(-172.3),
  ...               K.tilt(10),
  ...               K.range(1200),
  ...               K.altitudeMode("relativeToGround"),
  ...             )
  ...           )
  ...         )
  ...       )
  ... )
  >>> print schema.validate(doc)
  
""",
)
