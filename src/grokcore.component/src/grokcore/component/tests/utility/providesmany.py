"""
Subclasses of grok.GlobalUtility that are supposed to be registered
directly as utilities and which provide more than one interface must
specify which interface to use for the registration:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: <class 'grokcore.component.tests.utility.providesmany.Club'>
  provides more than one interface (use grok.provides to specify which one
  to use).
"""
import grokcore.component as grok
from zope import interface

class IClub(interface.Interface):
    pass

class ISpikyClub(interface.Interface):
    pass

class Club(grok.GlobalUtility):
    interface.classProvides(IClub, ISpikyClub)
    grok.direct()
