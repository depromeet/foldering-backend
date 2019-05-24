from rest_framework import serializers 
from .models import Link, Text, Image, Folder, User

class LinkSerializer(serializers.ModelSerializer): 
   class Meta: 
       model = Link 
       fields = '__all__' 

class TextSerializer(serializers.ModelSerializer): 
   class Meta: 
       model = Text 
       fields = '__all__' 

class ImageSerializer(serializers.HyperlinkedModelSerializer): 
   image = serializers.ImageField(use_url=True)
   
   class Meta: 
       model = Image
       fields = '__all__'

class FolderSerializer(serializers.ModelSerializer): 
    links = LinkSerializer(many=True, read_only=True)
    texts = TextSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta: 
       model = Folder
       fields = ('title', 'owner', 'id', 'datetime', 'links', 'texts', 'images')

class UserSerializer(serializers.ModelSerializer):
    userImage = serializers.ImageField(use_url=True)
    
    class Meta:
        model = User
        fields = '__all__'
