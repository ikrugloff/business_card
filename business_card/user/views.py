from django.shortcuts import render


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        pass
    else:
        # GET
        # нарисовать страницу где можно ввести данные
        return render(request, 'login.html')