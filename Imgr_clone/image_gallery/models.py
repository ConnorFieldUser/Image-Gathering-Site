from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Image(models.Model):
    created_user = models.ForeignKey('auth.user')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_times = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()
    private = models.BooleanField(default=False)
    graphic = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "http://static.srcdn.com/slir/w1000-h500-q90-c1000:500/wp-content/uploads/landscape-1456483171-pokemon2.jpg"


class Comment(models.Model):

    text = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
