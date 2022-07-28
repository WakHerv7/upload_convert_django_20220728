from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import os
from PIL import Image 

# filename = r'pin.png'
# img = Image.open(filename)
# img.save("pin2.ico",size=[(32,32)])
form =""
# Create your views here.
def favicon_image_view(request, document_root):

	if request.method == 'POST':
		form = FaviconForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()			
			# return HttpResponse(form.cleaned_data['icon_Img'].name)
			filename = form.cleaned_data['icon_Img'].name
			newname = form.cleaned_data['name']
			file_path = os.path.join(document_root,'images/', filename)
			# return HttpResponse(file_path)
			if os.path.exists(file_path):
				
				img = Image.open(file_path)
				img.save(document_root+"/favicons/"+newname+"-16.ico", format = 'ICO', sizes=[(16,16)])
				img.save(document_root+"/favicons/"+newname+"-32.ico", format = 'ICO', sizes=[(32,32)])
				img.save(document_root+"/favicons/"+newname+"-64.ico", format = 'ICO', sizes=[(64,64)])
				
				return redirect('success')
			return redirect('error_w')
	else:
		form = FaviconForm()
	return render(request, 'favicon_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

def error_w(request):
	return HttpResponse('There was an error !')
