from django.shortcuts import render


# Create your views here.
def about_view(request):
    f_name = 'Ilia'
    age = '30'
    return render(request, 'about.html',{'first_name': f_name, 'age': age})
