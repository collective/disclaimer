# -*- coding: utf-8 -*-
from plone import api


PROJECTNAME = 'collective.disclaimer'

# BBB: remove on deprecation of Plone 4.3
IS_BBB = api.env.plone_version().startswith('4.3')
