# -*- coding: utf-8 -*-
from OBS.Publication.content.publication import IPublication  # NOQA E501
from OBS.Publication.testing import OBS_PUBLICATION_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class PublicationIntegrationTest(unittest.TestCase):

    layer = OBS_PUBLICATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_publication_schema(self):
        fti = queryUtility(IDexterityFTI, name='Publication')
        schema = fti.lookupSchema()
        self.assertEqual(IPublication, schema)

    def test_ct_publication_fti(self):
        fti = queryUtility(IDexterityFTI, name='Publication')
        self.assertTrue(fti)

    def test_ct_publication_factory(self):
        fti = queryUtility(IDexterityFTI, name='Publication')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPublication.providedBy(obj),
            u'IPublication not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_publication_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Publication',
            id='publication',
        )

        self.assertTrue(
            IPublication.providedBy(obj),
            u'IPublication not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('publication', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('publication', parent.objectIds())

    def test_ct_publication_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Publication')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_publication_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Publication')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'publication_id',
            title='Publication container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
