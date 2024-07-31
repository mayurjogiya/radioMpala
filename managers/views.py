from django.shortcuts import render, redirect
from django.http import HttpResponse
from Surapuradada.models import *


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated and request.user.is_manager:
        manager = Managers.objects.get(managerId = request.user)
        stores = Stores.objects.filter(managerId = manager)
        active = Stores.objects.filter(activeStatus = True).count()
        inActive = Stores.objects.filter(activeStatus = False).count()
        return render(request, 'store-manage/index.html', { "details" : stores , "active" : active, "inActive" : inActive})
    else:
        return redirect('login')


def listen(request):
    if request.user.is_authenticated and request.user.is_manager:
        manager = Managers.objects.get(managerId = request.user)
        brand = Brands.objects.get(managerId = manager)
        return render(request, 'store-manage/listen.html', { "details" : brand })
    else:
        return redirect('login')