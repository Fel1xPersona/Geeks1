from django.db import models

# Create your models here.

class Team(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    status = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name="Фотография сотрудника"
    )
    email = models.EmailField(
        verbose_name="email"
    )
    instagram = models.URLField(
        verbose_name="instagram"
    )
    facebook = models.URLField(
        verbose_name="facebook"
    )
    telegram = models.URLField(
        verbose_name="telegram"
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    