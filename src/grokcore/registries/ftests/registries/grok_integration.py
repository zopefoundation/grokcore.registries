"""
  >>> root = {}
  >>> root['app'] = MyApplication()

  >>> gl = Example('local')

  >>> otherRegistry.registerUtility(gl, IExample, name="global")

  >>> from zope.component.hooks import setSite
  >>> from zope.component import getUtility

  >>> setSite(root['app'])
  >>> result = getUtility(IExample, name="global")
  >>> print str(result)
  local

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
  u"I am grabbed from local registry"


  >>> setSite()
"""

from zope.component import getGlobalSiteManager
from zope.interface import implements
from zope.component.registry import Components
from grokcore.registries import create_components_registry
from grokcore.registries.tests.registries.interfaces import IExample


otherRegistry = create_components_registry(name="otherRegistry", bases=(getGlobalSiteManager(),))


class Example(object):
    implements(IExample)

    def __init__(self, desc):
        self.desc = desc

    def __str__(self):
        return str(self.desc)


class MyApplication(object):

    def __init__(self):
        self._sm = Components()

    def getSiteManager(self):
        current = self._sm
        current.__bases__ += (otherRegistry,)
        return current
