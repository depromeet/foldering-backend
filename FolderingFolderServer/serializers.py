from rest_framework import serializers

from FolderingFolderServer.models import(
            Folder,
            Participation,
            Inclusion,
            Link,
            Text,
            Image
            )

class FolderModelSerializer(serializers.ModelSerializer):
   class Meta:
       model = Folder
       fields = ('id','folder_name', 'created_time', 'manager_id')

class FolderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('folder_name', 'manager_id')


class ParticipationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ('id','folder_uid', 'user_uid')

class InclusionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inclusion
        fields = ('id', 'folder_uid', 'data_uid', 'data_type')

class LinkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'link', 'folder_uid', 'created_time')

class TextModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'text', 'folder_uid', 'created_time')

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'iamge', 'folder_uid', 'created_time')


# from rest_framework import serializers
# from .models import Link, Text, Image, Folder
#
# class LinkSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Link
#        fields = '__all__'
#
# class TextSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Text
#        fields = '__all__'
#
# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#    image = serializers.ImageField(use_url=True)
#
#    class Meta:
#        model = Image
#        fields = '__all__'
#
# class FolderSerializer(serializers.ModelSerializer):
#     links = LinkSerializer(many=True, read_only=True)
#     texts = TextSerializer(many=True, read_only=True)
#     images = ImageSerializer(many=True, read_only=True)
#
#
#     class Meta:
#        model = Folder
#        fields = ('title','datetime', 'links', 'texts', 'images')