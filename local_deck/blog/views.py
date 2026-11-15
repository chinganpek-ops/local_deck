from django.shortcuts import get_object_or_404, render

from .constants import POSTS_ON_MAIN
from .models import Category, Post


def index(request):
    """Главная страница: 5 последних опубликованных публикаций."""
    post_list = Post.objects.published()[:POSTS_ON_MAIN]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    post = get_object_or_404(Post.objects.published(), id=id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.objects.published().filter(category=category)
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
