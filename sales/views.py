from django.shortcuts import render,redirect
from customers import models as customers_models
from products import models as products_models
from . import models, forms
# Create your views here.
def index(req):
	form = forms.Sale()
	saledetail = models.SaleDetail.objects.all()
	if req.POST:
		form = forms.Sale(req.POST)
		if form.is_valid():
			sale = form.save()
			return redirect('/sales/{}'.format(sale.id))
	sale = models.Sale.objects.all().order_by('date')
	return render(req, ('sales/index.html'), {
		'data' : sale,
		'form' : form,
		'detail' : saledetail,
		})

def sale_detail(req, id):
	form = forms.SaleDetail()
	salebyid = models.Sale.objects.filter(pk=id).first()
	if req.POST:
		form = forms.SaleDetail(req.POST)
		if form.is_valid():
			form.instance.sale = salebyid
			sale = form.save()
			stok_baru = sale.products.stok-sale.qty
			products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_baru)
	saledetail = models.SaleDetail.objects.filter(sale=salebyid)
	total=0
	for t in saledetail:
		total+=t.total()
	return render(req, ('sales/input_detail.html'), {
		'data' : saledetail,
		'form' : form,
		'sale' : salebyid,
		'total' : total,
		})
	
def transaksi(req):
	sale = models.Sale.objects.all()
	return render(req, ('transaksi/list_transaksi.html'), {
		'data' : sale,
		})

def input(req):
	return redirect('/sales', {
		'form' : form,
		})
	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	# stok_baru = products_models.stok+sale.qty
	# products_models.Prod.objects.filter(pk=products_models.id).delete(stok=stok_baru)
	return redirect('/sales')

def detail(req, id):
    sale = models.Sale.objects.filter(pk=id).all()
    return render(req, 'sales/detail.html', {
        'data': sale,
    })
