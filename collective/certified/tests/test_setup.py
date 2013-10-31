# -*- coding: utf-8 -*-
import unittest2 as unittest
from collective.certified.testing import INTEGRATION_TESTING
from collective.certified.config import PROJECTNAME

class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))
