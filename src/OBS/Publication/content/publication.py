# -*- coding: utf-8 -*-
from plone.app.textfield import RichText,RichTextValue
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.registry.interfaces import IRegistry
from Acquisition import aq_inner
from plone import api
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.content.interfaces import INameFromTitle

from zope import schema
from zope.interface import implementer
from zope.component import getUtility
import ads

# Set the ADS token to None to begin

ads.config.token = None

from OBS.Publication import _


class IPublication(model.Schema):
    """ Marker interface and Dexterity Python Schema for Publication
    """
    
    fieldset(
        'metadata',
        label = "Meta Data",
        description = "This data is automatically downloaded from ADS",
        fields=('pubtitle', 'authors', 'first_author','journal',
                'year', 'volume','page', 'abstract')
    )
    # ADS URL for the publication
    url = schema.TextLine(
        title=_(u'ADS Bibcode'),
        required=True
    )

    pubtitle = schema.TextLine(
        title='Title',
        required=False,
        #readonly=True
    )

    authors = schema.TextLine(
        title='Authors',
        required=False,
        #readonly=True
    )

    first_author = schema.TextLine(
        title='First Author',
        required=False,
        #readonly=True
    )

    journal = schema.TextLine(
        title='Journal',
        required=False,
        #readonly=True
    )

    year = schema.TextLine(
        title='Year',
        required=False,
        #readonly=True
    )

    volume = schema.TextLine(
        title='Volume',
        required=False,
        #readonly=True
    )

    page = schema.TextLine(
        title='Page',
        required=False
    )

    abstract = RichText(
        title='Abstract',
        required=False
    )



def postQuery(obj, event):
    '''After creating the object, do the query to get the data'''

    obj._query_data()
    return

@implementer(IPublication)
class Publication(Container):
    """ Content-type class for IPublication
    """
    
    def _query_data(self):
        '''Query the ADS database to retrieve the data'''
        if ads.config.token is None:
            registry = getUtility(IRegistry)
            ADStoken = registry['OBS.Publication.interfaces.IOBSPublicationSettings.ADStoken']
            ads.config.token = ADStoken
        
        try:
            paper = list(ads.SearchQuery(
                bibcode=self.url, 
                fl=['title','author','abstract','pub','year','volume','page','first_author']))[0]
        except ads.exceptions.APIResponseError:
            # Failed to query database
            portal = api.portal.get()
            messages = IStatusMessage(portal.REQUEST)
            messages.add(u"Warning: ADS database query failed", type=u"warning")
            return


        self.title = paper.title[0]
        self.first_author = paper.first_author
        self.authors = '; '.join(paper.author[:-1]) + "; and " + paper.author[-1]
        self.journal = paper.pub
        self.volume = paper.volume
        self.page = paper.page[0]
        self.year = paper.year

        self.abstract = RichTextValue(paper.abstract, 'text/html', 
                                           'text/html')
        return

    def Description(self):
        '''override the summar to be a journal-style citation'''
        summ = "{} et al. ({}), {}, {}, {}".format(self.first_author,
           self.year, self.journal, self.volume, self.page)
        return summ

class PublicationView(BrowserView):

    def ADSlink(self):
        """Return the ADS link."""

        context = aq_inner(self.context)
        link = "https://ui.adsabs.harvard.edu/abs/{}/abstract".format(context.url)
        return link

    def listDataFiles(self):
        '''Get listing of contained data files.'''
        return [t[1] for t in self.context.contentItems()]

class INameFromADS(INameFromTitle):
    def title():
        '''Return a processed title'''

@implementer(INameFromTitle)
class NameFromADS(object):

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return self.context.url

    
