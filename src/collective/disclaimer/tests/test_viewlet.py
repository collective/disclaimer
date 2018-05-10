# -*- coding: utf-8 -*-
from collective.disclaimer.testing import INTEGRATION_TESTING
from lxml import etree

import unittest


class DisclaimerViewletTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def toggle_disclaimer(self, enable):
        from plone.registry.interfaces import IRegistry
        from collective.disclaimer.interfaces import IDisclaimerSettings
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IDisclaimerSettings)  # noqa: P001
        self.settings.enabled = enable

    def get_viewlet_manager(self, context, name='plone.portalfooter'):
        from Products.Five.browser import BrowserView as View
        from zope.component import getMultiAdapter
        from zope.viewlet.interfaces import IViewletManager
        request = self.request
        view = View(context, request)
        manager = getMultiAdapter(
            (context, request, view), IViewletManager, name)
        return manager

    def get_viewlet(self, context, name='collective.disclaimer'):
        manager = self.get_viewlet_manager(context)
        manager.update()
        viewlet = [v for v in manager.viewlets if v.__name__ == name]
        assert len(viewlet) == 1
        return viewlet[0]

    def test_disclaimer_disabled(self):
        self.toggle_disclaimer(False)
        viewlet = self.get_viewlet(self.portal)
        html = etree.HTML(viewlet())
        div = html.xpath('//div[contains(@id,"viewlet-disclaimer")]')[0]
        self.assertEqual(div.attrib['data-enabled'], 'false')

    def test_disclaimer_enabled(self):
        from time import time
        self.toggle_disclaimer(True)
        self.settings.last_modified = now = str(time())
        viewlet = self.get_viewlet(self.portal)
        html = etree.HTML(viewlet())
        div = html.xpath('//div[contains(@id,"viewlet-disclaimer")]')[0]
        self.assertEqual(div.attrib['data-enabled'], 'true')
        self.assertEqual(div.attrib['data-last-modified'], now)
