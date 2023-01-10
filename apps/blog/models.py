from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='імя категорії', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія Блога'
        verbose_name_plural = 'Категорії Блога'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory,verbose_name='Категорія' ,on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок' , max_length=255)
    text_preview = models.TextField(verbose_name='Текст превю' , null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публікації')
    updated_date = models.DateTimeField(verbose_name='дата оновлення публікації' , auto_now=True)
    created_date = models.DateTimeField(verbose_name='дата створення публікації' , auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Стаття'

