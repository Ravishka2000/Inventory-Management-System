from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm


@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        "workers": workers,
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        "workers": workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        "items": items,
        "form": form,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    orders = Order.objects.all()

    context = {
        "orders": orders,
    }
    return render(request, 'dashboard/order.html', context)


