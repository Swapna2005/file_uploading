from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

  # Make sure to import your form

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()

    return render(request, 'file_upload.html', {'form': form})
    
        
def file_list(request):
            files = UploadedFile.objects.all()
            return render(request, 'file_list.html', {'files': files})
def file_download(request,file_id):
            uploaded_file = UploadedFile.objects.get(pk=file_id)
            response = HttpResponse(uploaded_file.file, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
            return response