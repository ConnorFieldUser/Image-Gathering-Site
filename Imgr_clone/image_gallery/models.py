from django.db import models

# Create your models here.


class Image(models.Model):
    created_user = models.ForeignKey('auth.user')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_times = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()
    private = models.BooleanField(default=False)
    graphic = models.BooleanField(default=False)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "http://static.srcdn.com/slir/w1000-h500-q90-c1000:500/wp-content/uploads/landscape-1456483171-pokemon2.jpg"
