# Generated by Django 2.1.7 on 2019-04-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FolderingAuthServer', '0003_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='token', max_length=255),
        ),
    ]