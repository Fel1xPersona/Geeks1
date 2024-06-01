from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовк"
    )
    email = models.EmailField(
        verbose_name="почта"
    )
    phone_number = models.PositiveIntegerField(
        verbose_name="Номер телефона"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настройки"