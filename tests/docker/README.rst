=====================================
Docker-based test environment for NAV
=====================================

This directory contains what you need to build and run a full NAV test
environment inside a Docker container. Assuming you have docker installed and
ready, you can use the included Makefile to build a Docker test environment
image and to run NAV's full test suite inside it - excellent for use on a
minimally provisioned CI server.

To build the Docker image, issue the :kbd:`make` command. To run the full test
suite on your checked out source code, inside a container, use :kbd:`make
check`.

Minimum requirements for a CI server
------------------------------------

A CI server to run the full NAV test suite needs only these things:

* Some CI software, e.g. Jenkins
* Git (to check out NAV's source code)
* Docker >= 1.0
* make
