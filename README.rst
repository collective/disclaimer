.. image:: https://raw.githubusercontent.com/collective/disclaimer/master/docs/disclaimer.png
    :align: left
    :alt: Disclaimer
    :height: 100px
    :width: 100px

**********
Disclaimer
**********

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

Show a disclaimer the first time a user visits a site.

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/collective.disclaimer.svg
   :target: https://pypi.python.org/pypi/collective.disclaimer

.. image:: https://img.shields.io/travis/collective/disclaimer/master.svg
    :target: http://travis-ci.org/collective/disclaimer

.. image:: https://img.shields.io/coveralls/collective/disclaimer/master.svg
    :target: https://coveralls.io/r/collective/disclaimer

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/disclaimer/issues

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

Edit your buildout.cfg and add the following to it:

.. code-block:: ini

    [buildout]
    ...
    eggs =
        collective.disclaimer

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to 'Disclaimer' and click the 'Activate' button.

Usage
-----

After installing the package,
go to the 'Disclaimer' configlet on 'Site Setup' and enable the feature.

.. figure:: https://raw.githubusercontent.com/collective/disclaimer/master/docs/configlet.png
    :align: center
    :height: 900px
    :width: 800px

    The Disclaimer control panel configlet.

Now, the first time a user visits the site the disclaimer will be shown at the bottom of the page.

.. figure:: https://raw.githubusercontent.com/collective/disclaimer/master/docs/viewlet.png
    :align: center
    :height: 600px
    :width: 800px

    The Disclaimer viewlet at work.

Users will see the disclaimer again whenever information in the configlet is updated.

How Does It Work?
-----------------

This package registers a new viewlet on ``plone.portalfooter`` viewlet manager.
The viewlet is normally hidden and it will only be shown after checking the user hasn't seen it yet.
The information on last time the viewlet was updated is stored in the user's browser local storage.
