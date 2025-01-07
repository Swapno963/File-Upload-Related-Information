from rest_framework import serializers
from .models import Document, FileUpload


# Storeing File on Database
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['name', 'file']  

# Storeing Document Related Character Data
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'content']

#   For getting all the fields, like : Title, Content, File Name, File 
class DocumentGetSerializer(serializers.ModelSerializer):
    fileUpload = FileUploadSerializer()
    class Meta:
        model = Document
        fields = ['title', 'content','fileUpload']
