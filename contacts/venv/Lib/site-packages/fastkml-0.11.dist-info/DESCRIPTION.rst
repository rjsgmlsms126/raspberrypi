Introduction
============

Fastkml is a library to read, write and manipulate KML files. It aims to keep
it simple and fast (using lxml_ if available). Fast refers to the time you
spend to write and read KML files as well as the time you spend to get
aquainted to the library or to create KML objects. It aims to provide all of
the functionality that KML clients such as `OpenLayers
<http://openlayers.org/>`_, `Google Maps <http://maps.google.com/>`_, and
`Google Earth <http://earth.google.com/>`_ provides.


Geometries are handled as pygeoif_ or, if installed, shapely_ objects.

.. _pygeoif: http://pypi.python.org/pypi/pygeoif/
.. _shapely: http://pypi.python.org/pypi/Shapely
.. _lxml: https://pypi.python.org/pypi/lxml
.. _dateutils: https://pypi.python.org/pypi/dateutils
.. _pip: https://pypi.python.org/pypi/pip

Fastkml is continually tested with *Travis CI*:

.. image:: https://api.travis-ci.org/cleder/fastkml.png
    :target: https://travis-ci.org/cleder/fastkml
    :alt: Tests

.. image:: https://coveralls.io/repos/cleder/fastkml/badge.png?branch=master
    :target: https://coveralls.io/r/cleder/fastkml?branch=master
    :alt: coveralls.io

.. image:: http://codecov.io/github/cleder/fastkml/coverage.svg?branch=master
    :target: http://codecov.io/github/cleder/fastkml?branch=master
    :alt: codecov.io

Is Maintained and documented:

.. image:: https://pypip.in/v/fastkml/badge.png
    :target: https://pypi.python.org/pypi/fastkml
    :alt: Latest PyPI version

.. image:: https://pypip.in/status/fastkml/badge.svg
    :target: https://pypi.python.org/pypi/fastkml/
    :alt: Development Status

.. image:: https://readthedocs.org/projects/fastkml/badge/
    :target: https://fastkml.readthedocs.org/
    :alt: Documentation

.. image:: https://badge.waffle.io/cleder/fastkml.png?label=ready&title=Ready
    :target: https://waffle.io/cleder/fastkml
    :alt: 'Stories in Ready'

.. image:: https://www.openhub.net/p/fastkml/widgets/project_thin_badge.gif
    :target: https://www.openhub.net/p/fastkml
    :alt: Statistics from OpenHub

Supports python 2 and 3:

.. image:: https://pypip.in/py_versions/fastkml/badge.svg
    :target: https://pypi.python.org/pypi/fastkml/
    :alt: Supported Python versions

.. image:: https://pypip.in/implementation/fastkml/badge.svg
    :target: https://pypi.python.org/pypi/fastkml/
    :alt: Supported Python implementations

Documentation
=============

You can find all of the documentation for FastKML at `fastkml.readthedocs.org
<https://fastkml.readthedocs.org>`_. If you find something that is missing,
please submit a pull request on `GitHub <https://github.com/cleder/fastkml>`_
with the improvement.


Install
========

You can install the package with ``pip install fastkml`` or ``easy_install
fastkml`` which should also pull in all requirements.

Requirements
-------------

* pygeoif_
* dateutils_

Optional
---------

* lxml_
* shapely_

You can install all of the requirements for working with FastKML by using
pip_::

    pip install -r requirements.txt

.. note::

    Shapely_ requires that libgeos be installed on your system. ``apt-get
    install libgeos-dev`` will install these requirements for you on Debian-
    based systems.


Limitations
===========

*Tesselate*, *Extrude* and *Altitude Mode* are assigned to a Geometry or
Geometry collection (MultiGeometry). You cannot assign different values of
*Tesselate*, *Extrude* or *Altitude Mode* on parts of a MultiGeometry.

Currently, the only major feature missing for the full Google Earth experience
is the `gx extension
<https://developers.google.com/kml/documentation/kmlreference#kmlextensions>`_.
This will most likely be added after the 1.0 version release.

You can find the complete list of current issues on `GitHub
<https://github.com/cleder/fastkml/issues>`_.

Changelog
=========

0.11.1 (2015/07/13)

- add travis deploy to travis.yml

0.11 (2015/07/10)
-----------------

-  handle coordinates tuples which contain spaces

0.10 (2015/06/09)
-----------------

- Fix bug when the fill or outline attributes of a PolyStyle are float strings

0.9 (2014/10/17)
-----------------

- Add tox.ini for running tests using tox [Ian Lee]
- Add documentation, hosted at https://fastkml.readthedocs.org [Ian Lee]

0.8 (2014/09/18)
-----------------

- Add support for address and phoneNumber [Ian Lee]
- Add support for Ground Overlay kml [Ian Lee]

0.7 (2014/08/01)
----------------

- Handle case where Document booleans (visibility,isopen) are 'true' or 'false' [jwhelland]
- test case additions and lxml warning [Ian Lee]
- pep8-ify source code (except test_main.py) [Ian Lee]
- pyflakes-ify source code (except __init__.py) [Ian Lee]

0.6 (2014/05/29)
----------------

- add Schema
- add SchemaData
- make use of lxmls default namespace

0.5 (2013/10/23)
-----------------

- handle big files with huge_tree for lxml [Egil Moeller]
- bugfixes


0.4 (2013/09/05)
-----------------

- adds the ability to add untyped extended data / named value pairs [Denis Krienbuehl]

0.3 (2012/11/15)
-----------------

- specify minor python versions tested with Travis CI
- add support for tesselation, altitudeMode and extrude to Geometries
- move implementation of geometry from kml.Placemark to geometry.Geometry
- add support for heterogenous GeometryCollection
- python 3 compatible
- fix test for python 3
- change license to LGPL
- register namespaces for a more pleasant, human readable xml output

0.2 (2012/07/27)
-----------------

- remove dependency on shapely
- add more functionality


0.1.1 (2012/06/29)
------------------

- add MANIFEST.in

0.1 (2012/06/27)
----------------

- initial release


