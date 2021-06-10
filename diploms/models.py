from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Topic(models.Model):
    """Класс темы сообщения для технической поддержки"""
    text = models.CharField(max_length=200)

    def __str__(self):
        """Возращает строковое представление модели."""
        return self.text


class Comment(models.Model):
    """Класс для комментария"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class City(models.Model):
    """Класс обозначающий доступные города для вакансий"""
    city = models.CharField(max_length=100, default='Москва')

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.city


class Vacansia(models.Model):
    """Класс для вакансий"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    image_url = models.CharField(max_length=500, default=' ')
    image_origin_str = models.CharField(max_length=100, default=' ')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'vacansies'

    def __str__(self):
        return self.name


class Message(models.Model):
    """Класс обращений"""
    title = models.ForeignKey(Topic, on_delete=models.CASCADE, default='Я ПОКУПАТЕЛЬ')
    text = models.TextField()
    file = models.FileField(null=True, blank=True,upload_to='diplom/media_cdn')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(null=True, blank=True, default=' ')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        if self.is_active:
            status = "Требуется решение!"
        else:
            status = "Решено!"

        if len(self.text) > 180:
            return status + ' ' + self.text[:180] + '...'
        else:
            return status + ' ' + self.text


class Interview(models.Model):
    """Класс записи на собеседование"""
    сandidate = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=11)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.first_name


class News(models.Model):
    """Класс новостей"""
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False, upload_to='media/')
    image_url = models.CharField(max_length=500, default=' ')
    image_origin_str = models.CharField(max_length=100, default=' ')
    origin = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Newses'

    def __str__(self):
        return self.title
