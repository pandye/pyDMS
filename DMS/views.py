from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from forms import uploadFileForm
from models import document
from django.template import RequestContext
import zipfile,tempfile
from django.core.servers.basehttp import FileWrapper
def home(request):
    if request.user.username:
        if request.method=="POST":
            #request.POST is a django.http.QueryDict object. So convert it to normal dictionary.
            p=dict(request.POST)
            for i in p["t"]:
                temp=document.objects.get(id=int(i))
                temp.doc.delete()
                temp.delete()
            return HttpResponseRedirect('/')
        else:
            documents = document.objects.filter(owner=request.user) 
            return render_to_response('home.html', {'user': request.user,'documents':documents},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
    
def login(request): 
    return render_to_response('login.html',{'user': request.user})

def uploadPage(request):
    if request.user.username:
        if request.method == 'POST':
            form = uploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = document(doc=request.FILES['file'],owner=request.user,docName=request.FILES['file'])
                newdoc.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Fill the upload form completely!")
        else:
            form = uploadFileForm() 
            return render_to_response('upload.html', {'form': form,'user': request.user},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')


def downloadPage(request,downloadfile,username):
    ''' This is used to download the file. This module converts file into zip 
    format then send it to user'''
    if request.user.username==username:
        temp = tempfile.TemporaryFile()
        archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
        #filename is absolute file path. change this according to your system
        filename = "/home/prakash/workspace/pyDMS/pyDMS/media/documents/"+request.user.username+"/"+downloadfile                          
        archive.write(filename, downloadfile)
        archive.close()
        wrapper = FileWrapper(temp)
        response = HttpResponse(wrapper, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s.zip'%downloadfile
        response['Content-Length'] = temp.tell()
        temp.seek(0)
        return response
    else:
        return HttpResponse("You are not authorized to download this file")


