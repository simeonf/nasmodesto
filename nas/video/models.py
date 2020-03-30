from django.db import models
from django.contrib.auth.models import User

class Klass(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name

class Video(models.Model):
    klass = models.ForeignKey(Klass, on_delete='cascade', verbose_name="Class")
    author = models.ForeignKey(User, on_delete='cascade')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=255)


    def class_name(self):
        return self.klass.name

    def __str__(self):
        return self.title

    
    def suffix(self):
        try:
            return self.youtube_link.split("/")[-1]
        except Exception:
            return ""
