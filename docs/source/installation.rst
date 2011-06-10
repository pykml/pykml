Installing pyKML
================

Linux Installation
~~~~~~~~~~~~~~~~~~

Installing the Dependencies
------------------------------------------

pyKML depends on the lxml_ Python library, which in turn depends on the 
libxml2_ and libxslt_ C libraries.  Given this, the first step to installing
pyKML is to get lxml running on your system (see `Installing lxml`_).

To verify that the lxml library has been installed correctly, 
open up a Python shell and type:

>>> import lxml
>>>

If you don't get back an error message, you are ready to proceed.

.. _lxml: http://codespeak.net/lxml
.. _Installing lxml: http://lxml.de/installation.html
.. _libxml2: http://xmlsoft.org/
.. _libxslt: http://xmlsoft.org/XSLT/


Installing the pyKML package
----------------------------

pyKML itself can be installed from the Python Package Index, 
using either pip_ or easy_install_::

    $ sudo easy_install pykml

or::

    $ sudo pip install pykml

To verify that the pyKML library has been installed correctly, 
open up a Python shell and type:

>>> import pykml
>>>

If you don't get back an error, head on over to the :doc:`tutorial`.

.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: http://packages.python.org/distribute/easy_install.html



.. todo:: TODO - describe installation on Windows
