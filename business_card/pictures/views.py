from django.shortcuts import render

# Create your views here.
def pictures_view(request):
    return render(request, 'pictures.html')
