from django.db import models

class User(models.Model):
    user_uid = models.IntegerField(unique=True) # oauth uid
    token = models.CharField(max_length=255, null=False) # Token 값

    class Meta:
        ordering = ["user_uid"]


