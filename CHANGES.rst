Changelog
=========

1.0b1 (2018-12-08)
------------------

- Register the controlpanel for any context.
  The correct registry is automatically acquired.
  This way, it's possible to set different disclaimer texts in a Lineage site with lineage.registry installed.
  [thet]

- Add a ``disclaimer-inner`` wrapper to allow easier styling, e.g. positioning the viewlet centered on the website and darkening the whole background.
  [thet]

- Move styles and scripts into the viewlet, so that they are included when using Diazo and just using the viewlet selector to copy the viewlet into the theme.
  [thet]

- Add an "OK" button instead of the close link.
  When the button is hit, the viewlet is closed and the storage key is set.
  Previously the storage key was immediately set even without using the "close" link.
  [thet]

- Fix translation of default values on configlet (HT @fredvd).
  [hvelarde]

- Fix style of hover and visited links inside disclaimer viewlet.
  [agnogueira]


1.0a1 (2018-05-14)
------------------

- Initial release.
