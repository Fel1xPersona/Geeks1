from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новсти"
    )
    description = models.TextField(
        verbose_name="Описание новости"
    )
    image = models.ImageField(
        upload_to="news/",
        verbose_name="Логотип"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"