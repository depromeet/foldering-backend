import datetime
from django.db import models
from FolderingAuthServer.models import User

class Folder(models.Model):
    folder_name = models.CharField(max_length=45, null=False,default=None) # 폴더 이름 입력은 필수로 함
    created_time = models.DateTimeField("Created Time",auto_now_add=True)
    manager_id = models.ForeignKey(
            User,
            related_name='FolderManagers',
            on_delete=models.CASCADE,
            null=False
            )

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return str(self.folder_name)


class Participation(models.Model):
    """
    어떤 폴더에 어떤 사용자가 참여하고 있는지 (어떤 사용자끼리 공유하고 있는지)
    """
    folder_uid = models.ForeignKey(
        Folder,
        related_name='FolderMember',
        on_delete=models.CASCADE
        )
    user_uid = models.ForeignKey(
            User,
            related_name='FolderMember',
            on_delete=models.CASCADE
            )

    class Meta:
        ordering = ["folder_uid"]

    def __str__(self):
        return str(self.folder_uid)


class Inclusion(models.Model):
    """
    어떤 폴더에 어떤 자료들이 포함되어 있는지
    """
    folder_uid = models.ForeignKey(
        Folder,
        related_name='FolderData',
        on_delete=models.CASCADE
        )
    data_uid = models.IntegerField()
    data_type = models.CharField(max_length=45,null=False,default=None)

    class Meta:
        ordering = ["folder_uid"]

    def __str__(self):
        return str(self.folder_uid)

class Link(models.Model):
    link = models.CharField(max_length=50, null=False)
    folder_uid = models.ForeignKey(
            Folder,
            null=True,
            related_name='linkData',
            on_delete=models.CASCADE
            )

class Text(models.Model):
    text = models.TextField(null=False)
    folder_uid = models.ForeignKey(
            Folder,
            null=True,
            related_name='textData',
            on_delete=models.CASCADE
        )

class Image(models.Model):
    image = models.ImageField(null=False)
    folder_uid = models.ForeignKey(
            Folder,
            null=True,
            related_name='imageData',
            on_delete=models.CASCADE
    )

#
# class Link(models.Model):
#     link = models.CharField(max_length=50, null = True)
#     folder = models.ForeignKey('Folder', null=True, related_name="links", on_delete=models.CASCADE)
#
# class Text(models.Model):
#     text = models.CharField(max_length=1000, null = True)
#     folder = models.ForeignKey('Folder', null=True, related_name="texts", on_delete=models.CASCADE)
#
# class Image(models.Model):
#     image = models.ImageField(default='media/default_image.jpeg', null = True)
#     folder = models.ForeignKey('Folder', null=True, related_name="images", on_delete=models.CASCADE)