from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from smtplib import SMTPException

# Register your models here.
from .models import UserUpload

class FoteReceiptNotExceptedError(Exception):
    """ Raised if receipt has not been accepted """

class UserUploadAdmin(admin.ModelAdmin):

    mail_subject = 'Subject'
    list_display = ['username', 'email', 'timestamp', 'upload_image', 'receipt_accepted', 'physical_mailing_list', 'sent_confirmation_email']
    ordering = list_display
    message = 'email template' #NOTE this would be replaced with the actual email template
    actions = ['send_email']

    #TODO unittest send_email
    def send_email(self, request, queryset):
        ''' send an email to the user with download link and update send status
         if successful self.message_user() to handle any exceptions here
        '''
        try:
            user = queryset[0]
            if not user.receipt_accepted:
                raise FoteReceiptNotExceptedError("The user's receipt must be marked as accepted before sending download email")

            send_mail(self.mail_subject, self.message, settings.DEFAULT_FROM_EMAIL, [user.email]) #NOTE this only send one email... might need to send to a collection of users
            user.sent_confirmation_email = True # set confirmation email to true 
            user.save()
            self.message_user(request, '<{} {}> download email has been sent successfully'.format(user.username, user.email))

        except FoteReceiptNotExceptedError as err:
            self.message_user(request, str(err), level=messages.ERROR)

        except SMTPException as err:
            # raise on an email send error
            self.message_user(request, '<{} {}> download email has not been send'.format(user.username, user.email), level=messages.ERROR)
            self.message_uer(request, 'SMTP Error: {}'.format(str(err)), level=messages.ERROR)

admin.site.register(UserUpload, UserUploadAdmin)
