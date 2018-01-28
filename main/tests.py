from django.test import TestCase

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
from .models import UserUpload
from .views import *
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_img_path = os.path.join(base_dir, 'test_img')

good_image = SimpleUploadedFile(name='baphomet.jpeg', content=open(test_img_path, 'rb').read(), content_type='image/jpeg')
bogus_image = SimpleUploadedFile(name='baphomet.jpeg', content=open(test_img_path, 'rb').read(), content_type='image/jpeg')

class UserUploadModelTests(TestCase):

    def test_create_user_upload_booleans_inits_to_false(self):
        record = {
            'username': 'hep',
            'email': 'hep@tup.com',
            'location': 'nyc',
            'upload_image': good_image
        }
        u = UserUpload(**record)

        # these are admin controlled fields
        self.assertIs(u.physical_mailing_list, False)
        self.assertIs(u.receipt_accepted, False)
        self.assertIs(u.sent_confirmation_email, False)

    def test_create_user_with_bad_email_throws_error(self):

        record = {
            'username': 'hep',
            'email': 'garbage',
            'location': 'nyc',
            'upload_image': good_image
        }
        with self.assertRaises(ValidationError):
            u = UserUpload(**record)
            u.full_clean()

    def test_create_user_upload_with_non_img_file_throws_error(self):

        record = {
            'username': 'hep',
            'email': 'gabage@garbage.com',
            'location': 'nyc',
            'upload_image': bogus_image
        }

        with self.assertRaises(ValidationError):
            u = UserUpload(**record)
            u.full_clean()
