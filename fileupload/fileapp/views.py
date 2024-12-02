from django.shortcuts import render,redirect,get_object_or_404
from .models import MediaFiles
from .forms import MediaFileForm
# Create your views here.
def upload_file(request):
    if request.method=='POST':
        form=MediaFileForm(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return redirect('file_list')
    else:
        form=MediaFileForm()

    return render(request,'fileapp/upload.html',{'form':form})

def file_list(request):
    files=MediaFiles.objects.all()
    file_data=[]
    for file in files:
        url=file.file.url.lower()
        file_data.append({
            'id':file.id,
            'title':file.title,
            'url':file.file.url,
            'type':"image" if url.endswith(('.jpg','.png','.jpeg','.gif')) else
            "video" if url.endswith(('.mp4','.avi','.mvk')) else
            "other"
        })
    return render(request,'fileapp/file_list.html',{'files':file_data})
def delete_file(request,file_id):
    file=get_object_or_404(MediaFiles,id=file_id)
    file.file.delete()
    file.delete()
    return redirect('file_list')

