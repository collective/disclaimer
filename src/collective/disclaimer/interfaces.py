# -*- coding: utf-8 -*-
from collective.disclaimer import _
from collective.disclaimer.config import IS_BBB
from plone import api
from plone.autoform import directives as form
from plone.supermodel import model
from time import time
from zope import schema
from zope.interface import Interface
from zope.interface import invariant


DEFAULT_DISCLAIMER = _(
    u'<p>We use cookies for statistical purposes, '
    u'to make the ads you see more relevant to you, '
    u'to help you sign up for our services, '
    u'or to remember your settings. '
    u'Check our <a>privacy and cookies policy</a>.</p>')


class IBrowserLayer(Interface):
    """A layer specific for this add-on product."""


class IDisclaimerSettings(model.Schema):
    """Schema for the control panel form."""

    enabled = schema.Bool(
        title=_(u'title_enabled', default=u'Enable disclaimer?'),
        description=_(
            u'help_enabled',
            default=u'If selected, a disclaimer will be shown the first time a user visits the site.'),  # noqa: E501
        default=False,
    )

    title = schema.TextLine(
        title=_(u'title_title', default=u'Title'),
        description=_(u'help_title', default=u'A title for the disclaimer.'),
        required=False,
        # XXX: can't use message id, string isn't being translated
        #      see: https://community.plone.org/t/6461
        default=_(u'Use of cookies'),
    )

    # XXX: we must use Text instead of RichText as we can only store
    #      primitive Python data types in plone.app.registry
    #      see: https://community.plone.org/t/1240
    if IS_BBB:
        # BBB: remove on deprecation of Plone 4.3
        from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
        form.widget('text', WysiwygFieldWidget)
    else:
        form.widget('text', klass='pat-tinymce')
    text = schema.Text(
        title=_(u'title_text', default=u'Body text'),
        description=_(u'help_text', default=u'The text of the disclaimer.'),
        required=True,
        # XXX: can't use message id, string isn't being translated
        #      see: https://community.plone.org/t/6461
        default=DEFAULT_DISCLAIMER,
    )

    last_modified = schema.ASCIILine(
        title=u'Last modified',
        description=u'The timestamp of last time the disclaimer was modified.',
        readonly=True,
    )

    @invariant
    def set_last_modified(data):
        """Store current timestamp on last_modified registry record.
        This invariant is used as a hook to update the timestamp, as
        its code is only executed when the form is saved.
        """
        name = IDisclaimerSettings.__identifier__ + '.last_modified'
        api.portal.set_registry_record(name, value=str(time()))
