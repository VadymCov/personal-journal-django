from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='entries', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'record'
        verbose_name_plural = 'records'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'tag'
        verbose_name_plural = 'tags'