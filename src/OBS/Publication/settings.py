'''Control panel settings for Publication'''
from OBS.Publication.interfaces import IOBSPublicationSettings
from OBS.Publication.interfaces import IOBSPublicationLayer
from plone.app.registry.browser import controlpanel
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


class OBSPublicationSettingsEditForm(controlpanel.RegistryEditForm):
    """
    Define form logic
    """
    schema = IOBSPublicationSettings
    label = u"Publication settings"

class OBSPublicationSettingsEditFormSettingsControlPanel(
    controlpanel.ControlPanelFormWrapper):

    form = OBSPublicationSettingsEditForm


@adapter(Interface, IOBSPublicationLayer)
class OBSPublicationSettingsConfigletPanel(RegistryConfigletPanel):
    """Control panel injection point"""

    schema = IOBSPublicationSettings
    configlet_id = "publication"
    configlet_category_id = "Products"
    title = "Publication settings"
    group = ""
    schema_prefix = "OBS.Publication.interfaces.IOBSPublicationSettings"