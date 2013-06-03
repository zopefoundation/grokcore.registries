import grokcore.component as grok
import grokcore.view as view

from zope.interface import Interface
from grokcore.registries.tests.registries.interfaces import IExample


class MyExample(grok.GlobalUtility):
    grok.name('local')
    grok.implements(IExample)


class PartyLayer(view.IBrowserRequest):
    pass

class Page(view.View):
    grok.context(Interface)

    def render(self):
        return u"I am grabbed from local registry"
