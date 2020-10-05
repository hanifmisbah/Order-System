from django.shortcuts import render, redirect
from sales import models as sales_models
from . import models, forms

# VIEWS ITEM/INDEX # VIEWS ITEM/INDEX # VIEWS ITEM/INDEX
def index(req):
	prod = models.Prod.objects.all().order_by('cate')
	return render(req, 'products/index.html', {
		'data' : prod,
		})

def category(req):
	cate = models.Cate.objects.all()
	return render(req, 'category/category.html', {
		'data' : cate,
		})

def stok_up(req, stok_stok):
	stok = sales_models.Sale.objects.get(pk=stok_stok)
	models.Prod.objects.update(stok=stok)
	return redirect('/products')

def stok_in(req):
	form = forms.Stok()

	if req.POST:
		form = forms.Stok(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/products/stok_in')
	
	prod = models.Stok.objects.all()
	return render(req, 'stok_in/stok_in.html', {
		'data' : prod,
		'form' : form,
		})

def input(req):
	form = forms.Prod()

	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/products')

	prod = models.Prod.objects.all()
	return render(req, 'products/input.html', {
		'data' : prod,
		'form' : form,
		})

def input_c(req):
	form = forms.Cate()

	if req.POST:
		form = forms.Cate(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/products/category')

	cate = models.Cate.objects.all()
	return render(req, 'category/input_category.html', {
		'data' : cate,
		'form' : form,
		})

def stok_in_input(req):
	form = forms.Stok()

	if req.POST:
		form = forms.Stok(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/products/stok_in')

	stok = models.Stok.objects.all()
	return render(req, 'category/stok_in.html', {
		'data' : stok,
		'form' : form,
		})

def update(req, id):
	products = models.Prod.objects.filter(pk=id).first()
	form = forms.Prod(instance=products)

	if req.POST:
		form = forms.Prod(req.POST, instance=products)
		if form.is_valid():
			form.save()
		return redirect('/products')

	prod = models.Prod.objects.filter(pk=id).first()
	return render(req, 'products/update.html', {
		'data' : prod,
		'form' : form,
		})

def delete(req, id):
	models.Prod.objects.filter(pk=id).delete()
	return redirect('/products')

def delete_c(req, id):
	models.Cate.objects.filter(pk=id).delete()
	return redirect('/products/category')

# def update_stok(req, id):
# 	form = forms.Prod()

# 	if req.GET:
# 		form = forms.Prod(req.GET)
# 		if form.is_valid():
# 			form.update()
# 			form.save()
# 		return redirect('/products')

# 	models.Stok.objects.filter(pk=id).update()

# # VIEWS CATEGORY # VIEWS CATEGORY # VIEWS CATEGORY # VIEWS CATEGORY
# def category(req):
# 	cate = models.Cate.objects.all()
# 	return render(req, 'category/category.html', {
# 		'data' : cate,
# 		})

# def input_category(req):
# 	if req.POST:
# 		models.Cate.objects.create(
# 			name = req.POST['name'])
# 		return redirect('/category/category')

# 	cate = models.Cate.objects.all()
# 	return render(req, 'category/input_category.html', {
# 		'data' : cate,
# 		})

# def update_category(req, id):
# 	if req.POST:
# 		models.Cate.objects.filter(pk=id).update(
# 			name = req.POST['name'])
# 		return redirect('/category')

# 	cate = models.Cate.objects.filter(pk=id).first()
# 	return render(req, 'category/update_category.html', {
# 		'data' : cate,
# 		})

# def delete_category(req, id):
# 	models.Cate.objects.filter(pk=id).delete()
# 	return redirect('/category/category')

# # VIEWS UNITS # VIEWS UNITS # VIEWS UNITS
# def units(req):
# 	unit = models.Units.objects.all()
# 	return render(req, 'units/unit.html', {
# 		'data' : unit,
# 		})

# def input_u(req):
# 	if req.POST:
# 		models.Units.objects.create(
# 			name = req.POST['name'])
# 		return redirect('/units/units')

# 	unit = models.Units.objects.all()
# 	return render(req, 'units/input.html', {
# 		'data' : unit,
# 		})

# def update_u(req, id):
# 	if req.POST:
# 		models.Units.objects.filter(pk=id).update(
# 			name = req.POST['name'])
# 		return redirect('/units')

# 	unit = models.Units.objects.filter(pk=id).first()
# 	return render(req, 'units/update.html', {
# 		'data' : unit,
# 		})

# def delete_u(req, id):
# 	models.Units.objects.filter(pk=id).delete()
# 	return redirect('/units/units')