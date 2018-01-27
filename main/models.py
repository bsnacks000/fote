from django.db import models


class UserUpload(models.Model):
    ''' a record of a user upload of a jpg receipt to the database'''

    username = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    upload_image = models.ImageField()

    def __str__(self):
        return self.username
