from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from Surapuradada.models import Stores, Managers, Logs
import datetime
import random, string


def listen(request):
    if request.user.is_authenticated and request.user.is_store:
        print(request.user)
        stores = Stores.objects.get(email = request.user.email)
        return render(request, 'temp-store/index.html', { 'details' : stores })
    elif request.user.is_authenticated and request.user.is_manager:
        return redirect('/manage')
    else:
        return redirect('/login')
        
def loginView(request):
    if request.method == 'POST':
        curUser = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if curUser is not None:
            login(request, curUser)
            inStr = ''.join(random.choices( string.digits + string.ascii_uppercase , k=5))
            logs = Logs.objects.create(
                logId = 'LOGIN_' + str(inStr),
                user = request.user,
                type = True,
                ipadd = 'not defiend',
                browser = request.META['HTTP_USER_AGENT'],
                stamp = datetime.datetime.now(),
                date = datetime.date.today()
            )
            print(logs)
            if curUser.is_store:
                store = Stores.objects.get(email = request.POST['email'])
                store.activeStatus = True
                store.save()
                return redirect('/')
            elif curUser.is_manager:
                manager = Managers.objects.get(email = request.POST['email'])
                manager.activeStatus = True
                manager.save()
                return redirect('/manage')
            elif curUser.is_superuser:
                return redirect('/surapura')
            else:
                return render(request, 'temp-store/login.html', {'status': False , 'erMsg' : 'You don\'t have Permission to visit this!' })
        else:
            return render(request, 'temp-store/login.html', {'status': False , 'erMsg' : 'Username or Password is Incorrect!'})
    else:
        return render(request, 'temp-store/login.html')
    
def logoutView(request):
    if request.user.is_anonymous is False:
        print(request.user)
        if request.user.is_store:
            store = Stores.objects.get(email = request.user.email)
            store.activeStatus = False
            store.save()
        elif request.user.is_manager:
            manager = Managers.objects.get(email = request.user.email)
            manager.activeStatus = False
            manager.save()
            
        outStr = ''.join(random.choices( string.digits + string.ascii_uppercase , k=5))
        logs = Logs.objects.create(
                    logId = 'LOGOUT_' + str(outStr),
                    user = request.user,
                    type = False,
                    ipadd = 'not defined',
                    browser = request.META['HTTP_USER_AGENT'],
                    stamp = datetime.datetime.now(),
                    date = datetime.date.today()
                )
        print('called logout')
        logout(request)
        return redirect('login')
    else:
        logout(request)
        return redirect('login')


