from django.shortcuts import render,redirect
from customers import models as customers_models
from products import models as products_models
from . import models, forms
# Create your views here.
def index(req):
	form = forms.Sale()

	if req.POST:
		form = forms.Sale(req.POST)
		if form.is_valid():
			sale = form.save()
			stok_baru = sale.products.stok-sale.qty
			products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_baru)
	sale = models.Sale.objects.all().order_by('date')
	return render(req, ('sales/index.html'), {
		'data' : sale,
		'form' : form,
		})

def transaksi(req):
	sale = models.Sale.objects.all()
	return render(req, ('transaksi/list_transaksi.html'), {
		'data' : sale,
		})

def input(req):
	form = forms.Sale()

	if req.POST:
		form = forms.Sale(req.POST)
		if form.is_valid():
			sale = form.save()
			stok_baru = sale.products.stok-sale.qty
			products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_baru)
	return redirect('/sales', {
		'form' : form,
		})
	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	return redirect('/sales')

def detail(req, id):
    sale = models.Sale.objects.filter(pk=id).all()
    return render(req, 'sales/detail.html', {
        'data': sale,
    })
