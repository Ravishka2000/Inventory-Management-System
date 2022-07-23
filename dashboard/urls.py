from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('product/delete/<str:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<str:pk>/', views.product_update, name='dashboard-product-update'),
]
