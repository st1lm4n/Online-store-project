from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')

class PostAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.has_perm('blog.add_post')