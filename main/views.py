from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserUploadForm

def index(request):
    ''' the index handler redirects to submission (essentially the main page of the app)'''
    return redirect('submission')


def submission(request):
    ''' user submits a jpg and metadata via form submission which is stored in the db
    on validation the user redirects to success route
    on failure the user redirects to failure route
    '''
    form = UserUploadForm()
    if request.method == 'POST':
        form = UserUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            messages.error(request, 'Some fields of the form are invalid')
    return render(request, 'main/submission.html', {'form':form})


def success(request):
    ''' on success handler renders the success.html template'''
    return render(request, 'main/success.html')
