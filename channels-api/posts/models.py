from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    likes = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return str(self.title)
    
class Statistic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    @property
    def data(self):
        return self.dataitem_set.all()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class DataItem(models.Model):

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    owner = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.owner} {self.value}'