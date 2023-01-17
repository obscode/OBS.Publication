.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.


===============
OBS.Publication
===============

A content type that queries the 
`NASA Astrophysics Data System (ADS)<https://ui.adsabs.harvard.edu/>`_
and retrieves the meta-data for a single academic publication. The user adds a publication 
content type to a folder. The only required field is the ADS biographical code. The rest of
the meta-data is downloaded automatically using the 
`ads module <https://github.com/andycasey/ads>`_ and fills in the other fields.

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
