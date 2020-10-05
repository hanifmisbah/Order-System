from django.db import models
from datetime import datetime
from django.utils import timezone
from customers import models as customers_models
from products import models as products_models
# Create your models here.
class Sale(models.Model):
	date = models.DateField(default=datetime.now)
	# cust = models.ForeignKey(customers_models.Cust, on_delete=models.CASCADE, related_name='membeli')
	products = models.ForeignKey(products_models.Prod, on_delete=models.CASCADE, related_name='terjual')
	qty = models.PositiveSmallIntegerField(default=0)
	desc = models.TextField(max_length=50)

	def __repr__(self):
		return self.products, self.date, self.qty, self.products.stok
	
	def total(self):
		return self.qty*self.products.price

	def stok(self):
		return self.products.stok-self.qty

	# def time(self, date):
	# 	return self.date_time.strftime("%c")