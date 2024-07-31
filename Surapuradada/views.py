from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
import random, string
from django.conf import settings  


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'surapura/index.html')
    else:
        return redirect('/login')

def stores(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            return render(request, 'surapura/stores.html')
        else:
            clients = Brands.objects.all()
            return render(request, 'surapura/stores.html', { 'clients': clients })
    else:
        return redirect('/login')

def addBrand(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            strId = ''.join(random.choices( string.digits + string.ascii_uppercase , k=5))
            brandObj = Brands.objects.create(
                brandId = 'STR'+ strId,
                managerId = Managers.objects.get(managerId = request.POST['managerId']) ,
                brandName = request.POST['storeName'],
                storeCount = request.POST['storeCount'],
                price = request.POST['storePrice'],
                startDate = request.POST['startDate'],
                embedLink = request.POST['embedLink'],
                imagePath = request.FILES['brandLogo'],
            )
            return render(request, 'surapura/add-brand.html')
        else:    
            return render(request, 'surapura/add-brand.html')
    else:
        return redirect('/login')
    
    

def showStores(request):
    if request.user.is_authenticated and request.user.is_superuser:
        bId = Brands.objects.get(brandId = request.GET['sId'])
        stores = Stores.objects.filter(brandId = bId)
        return render(request, 'surapura/show-stores.html', { 'brandId' : bId, 'Stores': stores })
    else:
        return redirect('/login')
    

def addStore(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            brandId = Brands.objects.get(brandId = request.GET['cId'])
            strId = ''.join(random.choices( string.digits + string.ascii_uppercase , k=3))
            userObj = User.objects.create_user(
                username = request.POST['storeEmail'],
                password = request.POST['storePassword'],
                email = request.POST['storeEmail'],
                is_store = True,
            )
            Store = Stores.objects.create(
                user = userObj,
                storeId = brandId.brandId + '_' + strId,
                brandId = brandId,
                managerId = brandId.managerId,
                email = request.POST['storeEmail'],
                password = request.POST['storePassword'],
                storeName = request.POST['storeName'],
                city = request.POST['storeCity'],
                location = request.POST['storeLocation'],
                contactNum = request.POST['storeNum'],
                storeCode = request.POST['embedLink'],
                activeStatus = False,
                activeDays = 0,
            )
            return render(request, 'surapura/add-store.html', { "brand": brandId })
        else:
            brandId = Brands.objects.get(brandId = request.GET['cId'])
            return render(request, 'surapura/add-store.html', { "brand": brandId })
    else:
        return redirect('/login')


def managers(request):
    if request.user.is_authenticated and request.user.is_superuser:
        managers = Managers.objects.all()
        return render(request, 'surapura/managers.html', { 'managers':managers })
    else:
        return redirect('/login')

def addManagers(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            userObj = User.objects.create_user(
                username = request.POST['managerEmail'],
                password = request.POST['managerPassword'],
                email = request.POST['managerEmail'],
                is_manager = True,
            )
            addmanager = Managers.objects.create(
                user = userObj,
                managerId = request.POST['managerEmail'],
                name = request.POST['managerName'],
                email = request.POST['managerEmail'],
                password = request.POST['managerPassword'],
                brandName = request.POST['brandName'],
                contactNum = request.POST['managerContact']
            )
            return render(request, 'surapura/add-manager.html')
        else:
            return render(request, 'surapura/add-manager.html')
    else:
        return redirect('/login')

def curActive(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'surapura/currentActive.html')
    else:
        return redirect('/login')

def report(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'surapura/report.html')
    else:
        return redirect('/login')