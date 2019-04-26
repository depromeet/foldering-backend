from rest_framework import serializers
from FolderingAuthServer.models import User

class UserModelSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('id', 'user_uid','token')