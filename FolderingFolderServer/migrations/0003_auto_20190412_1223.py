# Generated by Django 2.2 on 2019-04-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FolderingFolderServer', '0002_auto_20190411_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='title',
            new_name='link',
        ),
        migrations.AlterField(
            model_name='folder',
            name='image',
            field=models.ImageField(default='media/default_image.jpeg', null=True, upload_to=''),
        ),
    ]
