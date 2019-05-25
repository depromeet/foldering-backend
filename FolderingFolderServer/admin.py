from django.contrib import admin
from .models import Folder, Link, Text, Image

admin.site.register(Folder)
admin.site.register(Link)
admin.site.register(Text)
admin.site.register(Image)

