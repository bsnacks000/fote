# ModelForms for registration goes here

from django import forms
from .models import UserUpload


class UserUploadForm(forms.ModelForm):
    class Meta:
        model = UserUpload
        fields = ('username', 'email', 'location', 'upload_image', 'physical_mailing_list')
