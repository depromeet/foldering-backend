from django.db import models

class Folder(models.Model): 
    title = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now=True)

class Link(models.Model): 
    link = models.CharField(max_length=50, null = True)
    folder = models.ForeignKey('Folder', null=True, related_name="links", on_delete=models.CASCADE)

class Text(models.Model): 
    text = models.CharField(max_length=1000, null = True)
    folder = models.ForeignKey('Folder', null=True, related_name="texts", on_delete=models.CASCADE)

class Image(models.Model): 
    image = models.ImageField(default='media/default_image.jpeg', null = True)
    folder = models.ForeignKey('Folder', null=True, related_name="images", on_delete=models.CASCADE)

