from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(
                Q(status='published') |
                Q(author=user, status='draft')
            )
        return Post.objects.filter(status='published')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'status']
    success_url = '/log/'
    template_name = 'blog/post_form.html'
    permission_required = 'blog.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'status']
    template_name = 'blog/post_form.html'
    permission_required = 'blog.change_post'

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что пользователь имеет право или является автором
        if not (request.user.has_perm('blog.manage_blog_content') or
                self.get_object().author == request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = 'blog.delete_post'

    def dispatch(self, request, *args, **kwargs):
        # Разрешаем удаление только контент-менеджерам
        if not request.user.has_perm('blog.manage_blog_content'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)