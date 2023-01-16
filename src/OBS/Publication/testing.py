# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import OBS.Publication


class ObsPublicationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=OBS.Publication)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'OBS.Publication:default')


OBS_PUBLICATION_FIXTURE = ObsPublicationLayer()


OBS_PUBLICATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OBS_PUBLICATION_FIXTURE,),
    name='ObsPublicationLayer:IntegrationTesting',
)


OBS_PUBLICATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OBS_PUBLICATION_FIXTURE,),
    name='ObsPublicationLayer:FunctionalTesting',
)


OBS_PUBLICATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OBS_PUBLICATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ObsPublicationLayer:AcceptanceTesting',
)
