from catalog.models import Product
from django.shortcuts import render
from .models import Contact


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 продуктов:", list(latest_products))
    return render(request, 'catalog/home.html', {'products': latest_products})


def contacts(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')


