"""
  >>> root = {}
  >>> root['app'] = MyApplication()

  >>> from zope.component.hooks import setSite
  >>> from zope.component import getUtility

  >>> result = getUtility(IExample, name="global")
  >>> result
  <grokcore.registries.tests.registries.global.MyExample object at ...>

  >>> getUtility(IExample, name=u'local')
  Traceback (most recent call last):
  ...
  ComponentLookupError: (<InterfaceClass grokcore.registries.tests.registries.interfaces.IExample>, u'local')


  >>> setSite(root['app'])

  >>> result = getUtility(IExample, name=u'local')
  >>> result
  <grokcore.registries.tests.registries.local.MyExample object at 0...>


  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> from grokcore.component import Context
  >>> context = Context()
  >>> from zope.component import getMultiAdapter
  >>> view = getMultiAdapter((context, request), name='page')
  >>> view.render()
  u'I Am grabbed from GSM'


  >>> from zope.interface import alsoProvides
  >>> from grokcore.registries.tests.registries.local import PartyLayer
  >>> alsoProvides(request, PartyLayer)
  >>> view = getMultiAdapter((context, request), name='page')
  >>> view.render()
  u'I am grabbed from local registry'


  >>> setSite()
"""

from zope.interface import implements
from zope.component.registry import Components
from grokcore.registries import create_components_registry
from grokcore.registries.tests.registries.interfaces import IExample


from grokcore.registries.ftests.registries.basic import specialRegistry




class MyApplication(object):

    def __init__(self):
        self._sm = Components()

    def getSiteManager(self):
        current = self._sm
        current.__bases__ = (specialRegistry,) + current.__bases__
        return current

