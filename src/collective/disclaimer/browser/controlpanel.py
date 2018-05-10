# -*- coding: utf-8 -*-
from collective.disclaimer import _
from collective.disclaimer.interfaces import IDisclaimerSettings
from plone.app.registry.browser import controlpanel


class DisclaimerSettingsEditForm(controlpanel.RegistryEditForm):
    """Control panel edit form."""

    schema = IDisclaimerSettings
    label = _(u'Disclaimer')
    description = _(u'Show a disclaimer the first time a user visits a site.')


class DisclaimerSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Control panel form wrapper."""

    form = DisclaimerSettingsEditForm
