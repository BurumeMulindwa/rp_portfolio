from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class Meta:
    verbose_name_plural = 'categories'


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)