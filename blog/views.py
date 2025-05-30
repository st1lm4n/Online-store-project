from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Post
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    model = Post
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login/'
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
