# -*- coding: utf-8 -*-
from collective.disclaimer.interfaces import IDisclaimerSettings
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class DisclaimerViewlet(ViewletBase):
    """The disclaimer viewlet."""

    def update(self):
        super(DisclaimerViewlet, self).update()
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IDisclaimerSettings)  # noqa: P001

    def enabled(self):
        """Check if the disclaimer must be shown."""
        return str(self.settings.enabled).lower()

    def title(self):
        """Return the title of the disclaimer."""
        return self.settings.title

    def text(self):
        """Return the text of the disclaimer."""
        return self.settings.text

    def last_modified(self):
        """Return the timestamp of last time the disclaimer was modified."""
        return self.settings.last_modified
