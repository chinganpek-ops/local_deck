from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from .constants import (
    NAME_MAX_LENGTH,
    SLUG_MAX_LENGTH,
    STR_LIMIT,
    TITLE_MAX_LENGTH,
)


User = get_user_model()


class PublishedModel(models.Model):
    """Абстрактная модель с флагом публикации и датой создания."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        abstract = True


class PostManager(models.Manager):
    """Менеджер опубликованных постов."""

    def published(self):
        """Только опубликованные посты с прошедшей датой."""
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )


class Category(PublishedModel):
    """Тематическая категория публикаций."""

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name='Заголовок',
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы '
            'латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    def __str__(self):
        return self.title[:STR_LIMIT]

    class Meta(PublishedModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(PublishedModel):
    """Географическая метка."""

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name='Название места',
    )

    def __str__(self):
        return self.name

    class Meta(PublishedModel.Meta):
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(PublishedModel):
    """Публикация в блоге."""

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name='Заголовок',
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='posts',
        verbose_name='Категория',
    )

    objects = PostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)
