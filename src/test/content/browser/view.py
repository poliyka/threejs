from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from test.content import _


class Use(BrowserView):

    template = ViewPageTemplateFile('templates/use.pt')


    def __call__(self):
        return self.template()

