from django.db import models
  
# Create your models here.
class URL(models.Model):
    longurl = models.URLField(max_length=200)
    custom_name = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)


    def __str__(self):
        return self.custom_name