"""
Subclassed sites inherit all local utilities of their base classes:

  >>> cave = BigCave()
  >>> getRootFolder()["cave"] = cave

  >>> from zope import component
  >>> from zope.site.hooks import getSite, setSite

  >>> setSite(cave)
  >>> fireplace = component.getUtility(IFireplace)
  >>> IFireplace.providedBy(fireplace)
  True
  >>> isinstance(fireplace, Fireplace)
  True

Additional utilities can be registered in the subclass:
  
  >>> hollow = HollowCave()
  >>> getRootFolder()["hollow"] = hollow

  >>> setSite(hollow)
  >>> fireplace = component.getUtility(IFireplace)
  >>> IFireplace.providedBy(fireplace)
  True
  >>> isinstance(fireplace, Fireplace)
  True

  >>> painting = component.getUtility(IPainting)
  >>> IPainting.providedBy(painting)
  True
  >>> isinstance(painting, Painting)
  True

Those do not influence the base class:

  >>> setSite(cave)
  >>> painting = component.getUtility(IPainting)
  Traceback (most recent call last):
    ...
  ComponentLookupError: (<InterfaceClass grokcore.site.ftests.utility.subclass.IPainting>, '')

This works various levels of inheritance deep:

  >>> very_hollow = VeryHollowCave()
  >>> getRootFolder()['very_hollow'] = very_hollow

  >>> setSite(very_hollow)
  >>> fireplace = component.getUtility(IFireplace)
  >>> painting = component.getUtility(IPainting)
  >>> great_painting = component.getUtility(IPainting, 'great')
  >>> bad_painting = component.getUtility(IPainting, 'bad')

And with inheritance hierarchies where a base class is inherited multiple
times through different routes:

  >>> scary = ScaryCave()
  >>> getRootFolder()['scary'] = scary

  >>> setSite(scary)
  >>> fireplace = component.getUtility(IFireplace)
  >>> painting = component.getUtility(IPainting)
  >>> great_painting = component.getUtility(IPainting, 'great')
  >>> bad_painting = component.getUtility(IPainting, 'bad')

"""
import grokcore.site
from zope import interface

class IFireplace(interface.Interface):
    pass

class IPainting(interface.Interface):
    pass

class Fireplace(grokcore.site.LocalUtility):
    interface.implements(IFireplace)

class Painting(grokcore.site.LocalUtility):
    interface.implements(IPainting)

class Cave(grokcore.site.Site):
    # we use name_in_container here to prevent multiple registrations
    # since storing the utilities multiple times under the same name
    # would raise a DuplicationError
    grokcore.site.local_utility(Fireplace, name_in_container='fireplace')

class BigCave(Cave):
    pass

class HollowCave(Cave):
    grokcore.site.local_utility(Painting)

class VeryHollowCave(HollowCave):
    grokcore.site.local_utility(Painting, name='great')
    grokcore.site.local_utility(Painting, name='bad')

# this cave subclasses from Cave twice
class ScaryCave(VeryHollowCave, Cave):
    pass

