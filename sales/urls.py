from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('transaksi/', views.transaksi),
	path('input/', views.input),
	path('<id>/', views.sale_detail),
	path('<id>/delete', views.delete),
	# path('<id>/update', views.update),
	path('<id>/detail', views.detail),
]