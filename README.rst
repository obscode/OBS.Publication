.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/collective/OBS.Publication/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/OBS.Publication/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/OBS.Publication/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/OBS.Publication?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/OBS.Publication/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/OBS.Publication

.. image:: https://img.shields.io/pypi/v/OBS.Publication.svg
    :target: https://pypi.python.org/pypi/OBS.Publication/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/OBS.Publication.svg
    :target: https://pypi.python.org/pypi/OBS.Publication
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/OBS.Publication.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/OBS.Publication.svg
    :target: https://pypi.python.org/pypi/OBS.Publication/
    :alt: License


===============
OBS.Publication
===============

A content type that queries the NASA Abstract Data Service (ADS) and retrieves the
meta-data for a single academic publication. The user adds a publication content
type to a folder. The only required field is the ADS biographical code. The rest of
the meta-data is downloaded automatically (using [ads](https://github.com/andycasey/ads))
module and fills in the other fields.

Features
--------

- Not many at the moment, this is a work in progress. So far, the default folder
  listing will look "okay". A proper view is still needed.


Installation
------------

Install OBS.Publication by adding it to your buildout::

    [buildout]

    ...

    eggs =
        OBS.Publication


and then running ``bin/buildout``


Authors
-------

Chris Burns (Carnegie Observatories)


Contribute
----------

- Issue Tracker: https://github.com/collective/OBS.Publication/issues
- Source Code: https://github.com/collective/OBS.Publication
- Documentation: https://docs.plone.org/foo/bar


License
-------

The project is licensed under the GPLv2.
