from django.shortcuts import render
from .models import JsonDatas
from .resources import JsonResources
from tablib import Dataset
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def simple_upload(request):
    if request.method == 'POST':
        Json_Resources =  JsonResources()
        dataset = Dataset()
        myfile = request.FILES['myfile']

        if not myfile.name.endswith('json'):
            messages.info(request,'Wrong Format')
            return render(request,'wrongformat.html')

        imported_data = dataset.load(myfile.read(),format='json')
        for data in imported_data:
            print(data)
            value = JsonDatas(
                data[0],
                data[1],
                data[2],
                data[3]
            )
            value.save()
    return render(request,'index.html')

def jsonDataret(request):
    x = JsonDatas.objects.all()
    return render(request, "listofdata.html", {'jsonlist': x})