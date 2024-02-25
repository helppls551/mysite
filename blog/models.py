from django.db import models
from django.conf import  settings
from django.utils import  timezone
# Create your models here.


class MyPublish(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    #photo = models.ImageField(upload_to='img/%Y/%m/%d')
    publish_date = models.DateTimeField(blank=True,null=True)
    create_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
