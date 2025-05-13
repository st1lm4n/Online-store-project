from django.shortcuts import render, get_object_or_404
from .models import Contact, Product
from django.shortcuts import redirect
from .forms import ProductForm
from django.core.paginator import Paginator


def home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})


def home(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 6)  # 6 товаров на странице
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'products': products})
