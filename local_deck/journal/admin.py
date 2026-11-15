from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки отображения категорий в админке."""

    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Настройки отображения местоположений в админке."""

    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройки отображения публикаций в админке."""

    list_display = (
        'title',
        'author',
        'category',
        'pub_date',
        'is_published',
    )
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
