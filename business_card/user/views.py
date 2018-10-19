from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login/')


def login_view(request):
    if request.method == 'POST':
        # получить данные
        data = request.POST
        # login = data['login']
        login = data.get('login')  # Better get data with  method 'get'
        password = data.get('password')
        user = auth.authenticate(username=login, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            incorrect_credentials = 'Wrong login name or password.'
            return render(request, 'login.html', {'error': incorrect_credentials})
    else:
        # GET
        # нарисовать страницу где можно ввести данные
        return render(request, 'login.html')
