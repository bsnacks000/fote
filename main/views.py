from django.shortcuts import render, redirect

from .forms import UserUploadForm

def index(request):
    ''' the index handler redirects to submission (essentially the main page of the app)'''
    return redirect('submission')


def submission(request):
    ''' user submits a jpg and metadata via form submission which is stored in the db
    on validation the user redirects to success route
    on failure the user redirects to failure route
    '''
    if request.method == 'POST':
        raise NotImplementedError # form validation save to database
        # return redirect('success') or redirect('failure')

    form = UserUploadForm()
    return render(request, 'main/submission.html', {'form':form})


def success(request):
    ''' on success handler renders the success.html template'''
    return render(request, 'main/success.html')


def failure(request):
    ''' on failure handler renders the failure.html template'''
    return render(request,'main/failure.html')
