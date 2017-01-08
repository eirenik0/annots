===============================
Annots
===============================


.. image:: https://img.shields.io/pypi/v/annots.svg
        :target: https://pypi.python.org/pypi/annots

.. image:: https://img.shields.io/travis/infernion/annots.svg
        :target: https://travis-ci.org/infernion/annots

.. image:: https://readthedocs.org/projects/annots/badge/?version=latest
        :target: https://annots.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/infernion/annots/shield.svg
     :target: https://pyup.io/repos/github/infernion/annots/
     :alt: Updates


``annots`` is the package that allow to use Python 3.6 variable annotations in handy way. Thanks for inspiration to attrs_ library.


When you wrap a class with ``annots`` decorator ::

        import annot

        @annot.s
        class Account:
            __tablename__ = 'account'

            username: str
            password: str


Annots add class attribute annotations into ``__init__`` ::

        class Account:
            def __init__(self, username, password):
                self.username = str
                self.password = str


* Free software: MIT license
* Documentation: https://annots.readthedocs.io.


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _attrs: https://github.com/hynek/attrs
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

