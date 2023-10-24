from django.db import models


class Spotlight(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='spotlight_images')

    def __str__(self):
        return self.name
    

class SocialMedia(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='social_media_images')

    def __str__(self):
        return self.text