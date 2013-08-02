from collective.grok import gs
from inigo.intranetpolicy import MessageFactory as _

@gs.importstep(
    name=u'inigo.intranetpolicy', 
    title=_('inigo.intranetpolicy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('inigo.intranetpolicy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
