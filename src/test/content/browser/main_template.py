# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.interfaces import IMainTemplate
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer


@implementer(IMainTemplate)
class MainTemplate(BrowserView):

    main_template_name = 'templates/main_template.pt'

    def __call__(self):
        return ViewPageTemplateFile(self.template_name)

    @property
    def template_name(self):
            return self.main_template_name

    @property
    def macros(self):
        return ViewPageTemplateFile(self.template_name).macros
