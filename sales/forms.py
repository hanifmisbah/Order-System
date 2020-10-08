from django.forms import ModelForm

from . import models

class Sale(ModelForm):
	class Meta:
		model=models.Sale
		exclude=[]

class SaleDetail(ModelForm):
	class Meta:
		model=models.SaleDetail
		exclude=['sale']