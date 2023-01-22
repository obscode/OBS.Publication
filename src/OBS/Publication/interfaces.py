# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface

class IOBSPublicationLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IOBSPublicationSettings(Interface):

    ADStoken = schema.TextLine(
        title="ADS token",
        description="Token from ADS for querying",
        required=True,
    )