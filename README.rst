.. role:: python(code)
    :language: python


================
encrypted-config
================

Read and write partially encrypted configuration files.

.. image:: https://img.shields.io/pypi/v/encrypted-config.svg
    :target: https://pypi.org/project/encrypted-config
    :alt: package version from PyPI

.. image:: https://github.com/mbdevpl/encrypted-config/actions/workflows/python.yml/badge.svg?branch=main
    :target: https://github.com/mbdevpl/encrypted-config/actions
    :alt: build status from GitHub

.. image:: https://codecov.io/gh/mbdevpl/encrypted-config/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/mbdevpl/encrypted-config
    :alt: test coverage from Codecov

.. image:: https://api.codacy.com/project/badge/Grade/ba21a054e3cf4f278ad1822017ef1987
    :target: https://app.codacy.com/gh/mbdevpl/encrypted-config
    :alt: grade from Codacy

.. image:: https://img.shields.io/github/license/mbdevpl/encrypted-config.svg
    :target: NOTICE
    :alt: license

Because of asymmetric encryption, it enables users to create encrypted configuration files readable only by the target application.

.. contents::
    :backlinks: none


How to use
==========


As a library
------------

.. code:: python

    import encrypted_config


Details are to be decided.

As a command-line tool
----------------------

To be decided.


How to NOT use
==============

Running this library on an system to which anyone else has access is not secure.

If anyone else can access your private key, they can also decrypt the configuration.


Algorithms
==========

The library relies on RSA.


Requirements
============

Python version 3.8 or later.

Python libraries as specified in `<requirements.txt>`_.

Building and running tests additionally requires packages listed in `<test_requirements.txt>`_.

Tested on Linux, macOS and Windows.
