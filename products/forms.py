from django.forms import ModelForm
from . import models

class Prod(ModelForm):
	class Meta:
		model=models.Prod
		exclude=['owner']

	def __init__(self, *args, **kwargs):
		super(Prod, self).__init__(*args, **kwargs)
		self.fields['cate'].widget.attrs['class'] = 'form-control'
		self.fields['kode'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['price'].widget.attrs['class'] = 'form-control'
		self.fields['stok'].widget.attrs['class'] = 'form-control'


class Cate(ModelForm):
	class Meta:
		model=models.Cate
		exclude=['owner']

	def __init__(self, *args, **kwargs):
		super(Cate, self).__init__(*args, **kwargs)
		self.fields['name_c'].widget.attrs['class'] = 'form-control'	