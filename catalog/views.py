from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from blog.models import Post
from .forms import ProductForm
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    ordering = ['-created_at']


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


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
