from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorty = request.GET.get('sort')
    map = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    orderby = map.get(sorty, 'id')

    template = 'catalog.html'
    context = {
        'phones': Phone.objects.order_by(orderby)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)