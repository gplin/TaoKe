#-*- coding:utf-8 -*-
#author gplin @20130815
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.base import ModelState

class TaokeJSONEncoder(DjangoJSONEncoder):
	def default(self,o):
		if isinstance(o,ModelState):
			return None
		else:
			return super(TaokeJSONEncoder,self).default(o)
