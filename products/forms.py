from django.forms import ModelForm

from . import models

class Prod(ModelForm):
	class Meta:
		model=models.Prod
		exclude=[]

class Cate(ModelForm):
	class Meta:
		model=models.Cate
		exclude=[]

# class Stok(ModelForm):
# 	class Meta:
# 		model=models.Stok
# 		exclude=[]