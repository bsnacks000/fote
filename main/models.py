from django.db import models
from django.dispatch import receiver
import os

class UserUpload(models.Model):
    """ a record of a user upload of a jpeg receipt to the database
    """

    username = models.CharField(max_length=100) # username
    email = models.EmailField(unique=True)   # users email - must be unique
    location = models.CharField(max_length=200)   # user's location
    timestamp = models.DateTimeField(auto_now_add=True)  # time when user was added
    upload_image = models.ImageField(upload_to='user-uploads/%Y-%m-%d/')    # the receipt image (url link to image field stored in the db )
    receipt_accepted = models.BooleanField(default=False) # whether or not the user's receipt image was accepted by admin
    physical_mailing_list = models.BooleanField(default=False)  # whether or not the user wants to be added to physical release mailing list
    sent_confirmation_email = models.BooleanField(default=False) # whether or not the user has been emailed

    def __str__(self):
        return self.username


# NOTE these hooks were taken from a SO post on auto-delete hooks
@receiver(models.signals.post_delete, sender=UserUpload)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """ Deletes file from filesystem when corresponding `UserUpload` object is deleted.
    """
    if instance.upload_image:
        if os.path.isfile(instance.upload_image.path):
            os.remove(instance.upload_image.path)
