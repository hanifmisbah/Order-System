from django.forms import ModelForm

from . import models

class Sale(ModelForm):
	class Meta:
		model=models.Sale
		exclude=[]