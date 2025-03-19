from django.db import models



class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='static/profile', blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    intro = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    network = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    url = models.URLField()
    icon = models.ImageField(upload_to='static/icons')

    def __str__(self):
        return self.network
