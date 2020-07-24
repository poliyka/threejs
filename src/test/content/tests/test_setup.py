# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from test.content.testing import TEST_CONTENT_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that test.content is properly installed."""

    layer = TEST_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if test.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'test.content'))

    def test_browserlayer(self):
        """Test that ITestContentLayer is registered."""
        from test.content.interfaces import (
            ITestContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ITestContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TEST_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['test.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if test.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'test.content'))

    def test_browserlayer_removed(self):
        """Test that ITestContentLayer is removed."""
        from test.content.interfaces import \
            ITestContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ITestContentLayer,
            utils.registered_layers())
