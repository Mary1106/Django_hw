from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    content = models.TextField(verbose_name='Содержимое', blank=True, null=True)
    preview = models.ImageField(verbose_name='Превью', upload_to='blog/image', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', blank=True, null=True, auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)
    views_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['title']

