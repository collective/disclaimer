# -*- coding: utf-8 -*-
from collective.disclaimer.interfaces import IDisclaimerSettings
from collective.disclaimer.testing import INTEGRATION_TESTING
from collective.disclaimer.testing import QIBBB
from plone import api
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class ControlPanelTestCase(unittest.TestCase, QIBBB):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        view = api.content.get_view(
            u'disclaimer-settings', self.portal, self.request)
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@disclaimer-settings')

    def test_controlpanel_installed(self):
        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertIn('disclaimer', actions)

    def test_controlpanel_removed_on_uninstall(self):
        self.uninstall()  # BBB: QI compatibility

        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertNotIn('disclaimer', actions)


class RegistryTestCase(unittest.TestCase, QIBBB):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IDisclaimerSettings)  # noqa: E501, P001

    def test_enabled_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'enabled'))
        self.assertEqual(self.settings.enabled, False)

    def test_title_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'title'))
        self.assertIsNone(self.settings.title)

    def test_text_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'text'))
        self.assertIsNone(self.settings.text)

    def test_last_modified_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'last_modified'))
        self.assertIsNone(self.settings.last_modified)

    def test_records_removed_on_uninstall(self):
        self.uninstall()  # BBB: QI compatibility

        records = (
            IDisclaimerSettings.__identifier__ + '.enabled',
            IDisclaimerSettings.__identifier__ + '.title',
            IDisclaimerSettings.__identifier__ + '.text',
            IDisclaimerSettings.__identifier__ + '.last_modified',
        )

        for r in records:
            self.assertNotIn(r, self.registry)
