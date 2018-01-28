from django.test import TestCase

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
from .models import UserUpload
from .forms import UserUploadForm
from .views import *
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_img_path = os.path.join(base_dir, 'test_img', 'baphomet.jpeg')
bogus_img_path = os.path.join(base_dir, 'test_img', 'test_img.md')

good_image = SimpleUploadedFile(name='baphomet.jpeg', content=open(test_img_path, 'rb').read(), content_type='image/jpeg')
bogus_image = SimpleUploadedFile(name='test_img.md', content=open(bogus_img_path, 'rb').read(), content_type='text/plain')

class UserUploadModelTests(TestCase):

    def test_userupload_record_added_to_database(self):

        record = {'username': 'hep','email': 'hep@tup.com','location': 'nyc','upload_image': good_image}
        u = UserUpload(**record)
        u.save()

        get_user = UserUpload.objects.get(username='hep')
        self.assertIsEqual(len(get_user), 1)

    def test_create_user_upload_booleans_inits_to_false(self):
        record = {'username': 'hep','email': 'hep@tup.com','location': 'nyc','upload_image': good_image}

        u = UserUpload(**record)
        # these are admin controlled fields
        self.assertIs(u.physical_mailing_list, False)
        self.assertIs(u.receipt_accepted, False)
        self.assertIs(u.sent_confirmation_email, False)

    def test_create_user_with_bad_email_throws_validation_error(self):

        record = { 'username': 'hep', 'email': 'garbage', 'location': 'nyc', 'upload_image': good_image}

        with self.assertRaises(ValidationError):
            u = UserUpload(**record)
            u.full_clean() # catch the bad email here... NOTE this should be caught at the form level first...



class UserUploadFormTest(TestCase):

    def test_good_image_form_input_is_valid(self):

        data = {'username': 'hep','email': 'some@email.com','location': 'some location'}
        image_data = {'upload_image': good_image}

        form = UserUploadForm(data=data, files=image_data) # load good image
        self.assertTrue(form.is_valid())


    def test_bad_image_form_input_is_not_valid(self):

        data = {'username': 'hep','email': 'some@email.com','location': 'some location'}
        image_data = {'upload_image': bogus_image}

        form = UserUploadForm(data=data, files=image_data) # load bad image
        self.assertFalse(form.is_valid())


    def test_invalid_email(self):

        data = {'username': 'hep', 'email': 'blahblahblahblah','location': 'some location'}
        image_data = {'upload_image': good_image}

        form = UserUploadForm(data=data, files=image_data) # load bad image
        self.assertTrue(form.is_valid())
