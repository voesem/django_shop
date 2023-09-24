from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='превью (изображение)', **NULLABLE)
    publication_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
