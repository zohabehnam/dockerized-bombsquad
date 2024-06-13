
from playersData import pdata
import ba, setting
def addtag(node,player):
    session_player=player.sessionplayer
    account_id=session_player.get_account_id()
    customtag_=pdata.get_custom()
    customtag=customtag_['customtag']
    roles=pdata.get_roles()
    p_roles=pdata.get_player_roles(account_id)
    tag=None
    if account_id in customtag:
        tag=customtag[account_id]
    elif p_roles !=[]:
        for role in roles:

            if role in p_roles:
                tag=roles[role]['tag']
                break;
    if tag:
        Tag(node,tag)

from stats import mystats
def addrank(node,player):
	session_player=player.sessionplayer
	account_id=session_player.get_account_id()
	rank=mystats.getRank(account_id)

	if rank:
		Rank(node,rank)

def addhp(node):
    hp = node.hitpoints
    _set = setting.get_settings_data()
    def showHP():
        HitPoint(owner=node,prefix=str(int(hp)),position=(0,0.75,0),shad = 1.4)
    if hp: t = ba.Timer(100,ba.Call(showHP),repeat = True, timetype=ba.TimeType.SIM, timeformat=ba.TimeFormat.MILLISECONDS)

class Tag(object):
	def __init__(self,owner=None,tag="somthing"):
		self.node=owner
		mnode = ba.newnode('math',
                               owner=self.node,
                               attrs={
                                   'input1': (0, 1.5, 0),
                                   'operation': 'add'
                               })
		self.node.connectattr('torso_position', mnode, 'input2')
		if '\\' in tag:

			tag = tag.replace('\\d', ('\ue048'))
			tag = tag.replace('\\c', ('\ue043'))
			tag = tag.replace('\\h', ('\ue049'))
			tag = tag.replace('\\s', ('\ue046'))
			tag = tag.replace('\\n', ('\ue04b'))
			tag = tag.replace('\\f', ('\ue04f'))
			tag = tag.replace('\\g', ('\ue027'))
			tag = tag.replace('\\i', ('\ue03a'))
			tag = tag.replace('\\m', ('\ue04d'))
			tag = tag.replace('\\t', ('\ue01f'))
			tag = tag.replace('\\bs', ('\ue01e'))
			tag = tag.replace('\\j', ('\ue010'))
			tag = tag.replace('\\e', ('\ue045'))
			tag = tag.replace('\\l', ('\ue047'))
			tag = tag.replace('\\a', ('\ue020'))
			tag = tag.replace('\\b', ('\ue00c'))

		self.tag_text = ba.newnode('text',
                                          owner=self.node,
                                          attrs={
                                              'text': tag,
                                              'in_world': True,
                                              'shadow': 1.0,
                                              'flatness': 1.0,
                                              'color': (1,0.6,0.7),
                                              'scale': 0.01,
                                              'h_align': 'center'
                                          })
		mnode.connectattr('output', self.tag_text, 'position')

class Rank(object):
	def __init__(self,owner=None,rank=99):
		self.node=owner
		mnode = ba.newnode('math',
                               owner=self.node,
                               attrs={
                                   'input1': (0, 1.2, 0),
                                   'operation': 'add'
                               })
		self.node.connectattr('torso_position', mnode, 'input2')
		self.rank_text = ba.newnode('text',
                                          owner=self.node,
                                          attrs={
                                              'text': "#"+str(rank),
                                              'in_world': True,
                                              'shadow': 1.0,
                                              'flatness': 1.0,
                                              'color': (1,1,1),
                                              'scale': 0.01,
                                              'h_align': 'center'
                                          })
		mnode.connectattr('output', self.rank_text, 'position')

class HitPoint(object):
    def __init__(self,position = (0,1.5,0),owner = None,prefix = 'ADMIN',shad = 1.2):
        _set = setting.get_settings_data()
        if not _set['enablehptag']: return
        self.position = position
        self.owner = owner
        m = ba.newnode('math', owner=self.owner, attrs={'input1': self.position, 'operation': 'add'})
        self.owner.connectattr('position', m, 'input2')
        prefix = int(prefix) / 10
        preFix = u"\ue047" + str(prefix) + u"\ue047"
        self._Text = ba.newnode('text',
                                          owner=self.owner,
                                          attrs={
                                              'text':preFix,
                                              'in_world':True,
                                              'shadow':shad,
                                              'flatness':1.0,
                                              'color':(1,1,1) if int(prefix) >= 20 else (1.0,0.2,0.2),
                                              'scale':0.01,
                                              'h_align':'center'})
        m.connectattr('output', self._Text, 'position')
        def a():
            self._Text.delete()
            m.delete()
        self.timer = ba.Timer(100, ba.Call(a), timetype=ba.TimeType.SIM, timeformat=ba.TimeFormat.MILLISECONDS)