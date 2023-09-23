from django.shortcuts import render

from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product.html', locals())
