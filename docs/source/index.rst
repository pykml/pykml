.. pyKML documentation master file, created by
   sphinx-quickstart on Fri Apr 15 20:57:24 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyKML
================

pyKML is a Python package for creating, parsing, manipulating, and validating 
KML_, a language for encoding and annotating geographic data.

pyKML is based on the `lxml.objectify API`_ which provides a Pythonic API 
for working with XML documents.  pyKML adds additional functionality specific 
to the KML language.

KML comes in several flavors.   pyKML can be used with KML documents that 
follow the base `OGC KML`_ specification, the `Google Extensions Namespace`_, 
or a user-supplied extension to the base KML specification (defined by an XML
Schema document).

pyKML is open source. 
`Packaged releases`_ can be found on the 
Python Package Index (PyPI). 
Developers can download the `pyKML source code`_ and noodle with it.
`Bug reports, enhancement requests`_ and examples of using pyKML are appreciated.


.. _KML: http://code.google.com/apis/kml/documentation/
.. _OGC KML: http://www.opengeospatial.org/standards/kml/
.. _Google Extensions Namespace: http://code.google.com/apis/kml/documentation/kmlreference.html#kmlextensions
.. _lxml.objectify API: http://codespeak.net/lxml/objectify.html
.. _Packaged releases: http://pypi.python.org/pypi/pykml
.. _pyKML source code: http://code.google.com/p/pykml/
.. _Bug reports, enhancement requests: http://code.google.com/p/pykml/

Contents
==================

.. toctree::
    :maxdepth: 2

    installation
    tutorial
    examples
    modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

