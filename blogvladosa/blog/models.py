from django.db import models
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(
        max_length=255,
        help_text='Название категории',
        unique=True,
        verbose_name='Категория',
        db_column='category',
        db_comment='Название категории. Ограничение на 255 символов'
    )
    description = models.CharField(
        max_length=255,
        help_text='Описание категории',
        verbose_name='Описание',
        db_column='description',
        db_comment='Описание категории. Ограничение на 255 символов'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text='Слаг для категорий',
        verbose_name='URL',
        db_column='slug',
        db_comment='Слаг, помогающий сформировать url адрес для конкретной категории. '
                   'Ограничение на 255 символов'
    )

    class Meta:
        db_table = 'category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table_comment = 'Категории для постов'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(
        max_length=255,
        help_text='Заголовок поста',
        verbose_name='Пост',
        db_column='title',
        db_comment='Заголовок поста. Ограничение на 255 символов'
    )
    content = models.TextField(
        help_text='Наполнение статьи',
        verbose_name='Контент',
        db_column='content',
        db_comment='Текстовое наполнение статьи'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        help_text='Время создание поста',
        verbose_name='Время создания',
        db_column='time_create',
        db_comment='Время создание поста'
    )
    time_update = models.DateTimeField(
        auto_now=True,
        help_text='Время последнего обновления поста',
        verbose_name='Время обновления',
        db_column='time_update',
        db_comment='Время последнего обновления поста'
    )
    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.DRAFT,
        help_text='Статус публикации',
        verbose_name='Публикация',
        db_column='is_published',
        db_comment='Статус публикации поста'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Категория поста',
        verbose_name='Категория',
        db_column='category'
    )

    class Meta:
        db_table = 'post'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        db_table_comment = 'Посты пользователей'

    objects = models.Manager()
    published = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_pk': self.pk})
