from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    fileUpload = models.ForeignKey(FileUpload, related_name='documents', on_delete=models.CASCADE, null=True)
