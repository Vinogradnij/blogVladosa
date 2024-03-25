# Generated by Django 5.0.3 on 2024-03-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', db_comment='Заголовок поста. Ограничение на 255 символов', help_text='Заголовок поста', max_length=255, verbose_name='Пост')),
                ('content', models.TextField(db_column='content', db_comment='Текстовое наполнение статьи', help_text='Наполнение статьи', verbose_name='Контент')),
                ('time_create', models.DateTimeField(auto_now_add=True, db_column='time_create', db_comment='Время создание поста', help_text='Время создание поста', verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, db_column='time_update', db_comment='Время последнего обновления поста', help_text='Время последнего обновления поста', verbose_name='Время обновления')),
                ('is_published', models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], db_column='is_published', db_comment='Статус публикации поста', default=0, help_text='Статус публикации', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': ('пост',),
                'verbose_name_plural': ('посты',),
                'db_table': 'post',
                'db_table_comment': 'Посты пользователей',
            },
        ),
    ]
