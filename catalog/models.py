from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.BooleanField(default=True, verbose_name='создан')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)
