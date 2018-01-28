from django.db import models


class UserUpload(models.Model):
    ''' a record of a user upload of a jpg receipt to the database'''

    username = models.CharField(max_length=100) # username
    email = models.EmailField()   # users email
    location = models.CharField(max_length=200)   # user's location
    timestamp = models.DateTimeField(auto_now_add=True)  # time when user was added
    upload_image = models.ImageField()    # the receipt image (url link to image field stored in the db )
    receipt_accepted = models.BooleanField(default=False) # whether or not the user's receipt image was accepted by admin
    physical_mailing_list = models.BooleanField(default=False)  # whether or not the user wants to be added to physical release mailing list
    sent_confirmation_email = models.BooleanField(default=False) # whether or not the user has been emailed

    def __str__(self):
        return self.username
