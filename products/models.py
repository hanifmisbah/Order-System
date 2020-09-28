from django.db import models
from sales import models as sales_models
# Create your models here.
class Cate(models.Model):
	name_c = models.CharField(default='', max_length=30)

	def __str__(self):
		return self.name_c	

class Prod(models.Model):
	cate = models.ForeignKey(Cate, on_delete=models.CASCADE, related_name='termasuk')
	kode = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	price = models.PositiveIntegerField(default=0)
	stok = models.PositiveSmallIntegerField(default=0)

	def __repr__(self):
		return self.cate

	def __str__(self):
		return "{} - {}".format(self.kode, self.name)


class Stok(models.Model):
	name = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='tersedia')
	qty = models.PositiveSmallIntegerField(default=0)