
import json
import logging
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import staintools
import base64
from PIL import Image
import os
from django.http import FileResponse, HttpResponseServerError

def upload(request):
    return render(request, "upload.html")

@csrf_exempt
def update_img(request):
    if request.method == "PATCH":
        img_data = json.loads(request.body).get('imageFile').split(',')[1]
        img_binary = base64.b64decode(img_data)
        img_file_path = os.path.join('main/static/images', 'image.png')
        with open(img_file_path, 'wb') as f:
            f.write(img_binary)
        target = staintools.read_image("main/static/images/target.tiff")
        to_transform = staintools.read_image(img_file_path)
        target = staintools.LuminosityStandardizer.standardize(target)
        to_transform = staintools.LuminosityStandardizer.standardize(to_transform)
        normalizer = staintools.StainNormalizer(method='macenko')
        normalizer.fit(target)
        transformed = normalizer.transform(to_transform)
        print(transformed)
        img = Image.fromarray(transformed, "RGB")
        img.save('main/static/images/outputs/outputimg.png')
        context = {'image_path': 'main/static/images/outputs/outputimg.png'}
    return HttpResponse("success")


@csrf_exempt
def post_img(request):
    image_path = "/main/static/images/outputs/outputimg.png"
    context = {'image_path': image_path}
    return render(request, 'image.html', context)

    


    
