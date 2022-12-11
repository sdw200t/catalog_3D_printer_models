from django.shortcuts import render
from django.core.paginator import Paginator

import os

def index(request):
    template = 'models3D/listmodels.html'
    page_number = int(request.GET.get('page', 1))
    content = os.listdir('files/')
    paginator = Paginator(content, 12)
    page_models = paginator.get_page(page_number)
    list_models = []
    for sample in page_models:
        path_image = 'files/'+sample+'/images'
        if os.path.isdir(path_image): 
            images = os.listdir(path_image)
            if len(images)>0:
                list_models.append({'name':sample, 'image':'/'+path_image+'/'+images[0]})
            else:
                list_models.append({'name':sample, 'image':''})
        else:
            list_models.append({'name':sample, 'image':''})

    context = {
        'page_number': page_number,
        'page_models': page_models,
        'list_models': list_models,
    }
    return render(request, template, context)

def model(request, param_model):
    template = 'models3D/model_view.html'
    path_image = 'files/'+param_model+'/images'
    if os.path.isdir(path_image): 
        images = os.listdir(path_image)
        content = []
        for image in images:
            content.append({'image':'/'+path_image+'/'+image, 'name':image})
    else:
        content = []
    context = {
        'name': param_model,
        'content': content,
    }
    return render(request, template, context)