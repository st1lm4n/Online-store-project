from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from blog.models import Post
from .forms import ProductForm
from .models import Product
from ..services import get_products_by_category


@method_decorator(cache_page(60 * 15), name='dispatch')  # Кеш на 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class CategoryProductsView(ListView):
    template_name = 'products/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return get_products_by_category(category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        return context


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    ordering = ["-created_at"]


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "catalog/add_product.html", {"form": form})


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login/'
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('products.delete_product'):
            raise PermissionDenied("У вас нет прав для удаления этого продукта")
        return super().dispatch(request, *args, **kwargs)


class UnpublishProductView(PermissionRequiredMixin, UpdateView):
    permission_required = 'products.can_unpublish_product'
    model = Product
    fields = []

    def form_valid(self, form):
        form.instance.publish_status = 'draft'
        return super().form_valid(form)
