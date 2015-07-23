from collective.grok import gs
from samahan.policy import MessageFactory as _

@gs.importstep(
    name=u'samahan.policy', 
    title=_('samahan.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('samahan.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
