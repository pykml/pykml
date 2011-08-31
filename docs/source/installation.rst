Installing pyKML
================

Linux Installation
~~~~~~~~~~~~~~~~~~

Installing the Dependencies
------------------------------------------

pyKML depends on the lxml_ Python library, which in turn depends on two 
C libraries: libxml2_ and libxslt_.  Given this, the first step to installing
pyKML is to get lxml running on your system.  Refer to the `lxml` website for
`instructions on how to install lxml`_.

To verify that the lxml library has been installed correctly, 
open up a Python shell and type:

>>> import lxml
>>>

If you don't get back an error message, lxml has been installed and you are 
ready to proceed.

.. _lxml: http://codespeak.net/lxml
.. _instructions on how to install lxml: http://lxml.de/installation.html
.. _libxml2: http://xmlsoft.org/
.. _libxslt: http://xmlsoft.org/XSLT/


Installing the pyKML package
----------------------------

pyKML itself can be installed from the Python Package Index, 
using either pip_ or easy_install_::

    $ pip install pykml

or::

    $ easy_install pykml

To verify that the pyKML library has been installed correctly, 
open up a Python shell and type:

>>> import pykml
>>>

Once again, if you don't get back an error, pyKML has been installed correctly. 
To learn how to start using pyKML, head on over to the :doc:`tutorial`.

.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: http://packages.python.org/distribute/easy_install.html


.. todo:: TODO - describe installation on Windows

Building pyKML documentation
----------------------------

The pyKML documentation is built using Sphinx_ and uses the 
`ipython_directive`_ extension provided by the matplotlib_ project.  
Because of this, building the documentation requires that 
Sphinx_ 1.0, ipython_ and matplotlib_ be installed on your system.

.. note::
    Note that there appears to be a bug that prevents building documentation 
    when using the Ubuntu 10.04's default versions of the libraries.  The 
    documentation has been successfully built using the default libraries of 
    Ubuntu 11.04.

.. _Sphinx: http://sphinx.pocoo.org/
.. _ipython: http://ipython.org/
.. _ipython_directive: http://matplotlib.sourceforge.net/sampledoc/ipython_directive.html
.. _matplotlib: http://matplotlib.sourceforge.net/
