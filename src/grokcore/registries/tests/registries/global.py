import grokcore.component as grok
from grokcore.component.interfaces import IContext
import grokcore.view as view
from zope.interface import Interface
from grokcore.registries.tests.registries.interfaces import IExample


class MyExample(grok.GlobalUtility):
    grok.name('global')
    grok.implements(IExample)


class Page(view.View):
    grok.context(IContext)

    def render(self):
        return u"I Am grabbed from GSM"
