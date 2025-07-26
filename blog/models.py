from email.mime import audio
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='image/')
    audio = models.FileField(blank=True, null=True, upload_to='audio/')
    video = models.FileField(blank=True, null=True, upload_to='video/')
    # The upload_to parameter specifies the directory within MEDIA_ROOT where files will be stored
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title