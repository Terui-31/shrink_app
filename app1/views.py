from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings
import math



def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        max_id = Document.objects.latest('id').id
        obj = Document.objects.get(id = max_id)
        input_path = settings.BASE_DIR + obj.photo.url
        output_path = settings.BASE_DIR + "/media/output/output.jpg"
        shrink(input_path,output_path)

    return render(request, 'app1/index.html', {
        'form': form,
        'obj':obj,
    })


######################################

def shrink(input_path,output_path):
    img = cv2.imread(input_path)
    height, width = img.shape[0], img.shape[1]
    img2 = cv2.resize(img , (int(width*0.25), int(height*0.25)))
    cv2.imwrite(output_path, img2, [int(cv2.IMWRITE_JPEG_QUALITY), 80])

######################################