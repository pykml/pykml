The Sphinx_ package is used to create the pyKML documentation, including the 
`autodocumentation extension`_. Great examples of including equations and figures can be found in matplotlib's
`Documenting matplotlib`_ web page and the `matplotlib sampledoc tutorial`_.

Dependencies
=============

The pyKML documentation uses matplotlib and its Sphinx extensions. 
On Ubuntu 10.04, you can install matplotlib as follows:: 

    # the following doesn't work... matplotlib install generates error
    apt-get install freetype6 freetype6-dev
    pip install numpy
    pip install matplotlib
    pip install -f http://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.0.1/matplotlib-1.0.1.tar.gz matplotlib

    # installing matplotlib via apt-get
    apt-get install python-matplotlib
    mkvirtualenv pykml-doc
    pip install sphinx
    pip install -e hg+https://tylerickson@pykml.googlecode.com/hg#egg=pykml

Generating documentation
========================
To generate documentation for the project,
go to the docs/ folder and run the command::

    make html

.. _Sphinx: http://sphinx.pocoo.org/
.. _autodocumentation extension: http://sphinx.pocoo.org/ext/autodoc.html
.. _Documenting matplotlib: http://matplotlib.sourceforge.net/devel/documenting_mpl.html
.. _matplotlib sampledoc tutorial: http://matplotlib.sourceforge.net/sampledoc/
.. _ipython directive: http://matplotlib.sourceforge.net/sampledoc/ipython_directive.html

.. target-notes::

Running doctests
----------------
To run test snippets contained within the documentation, run the following:

    make doctest


