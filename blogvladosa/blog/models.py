from django.db import models
from django.urls import reverse


class Post(models.Model):
    pass


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
