from django.shortcuts import render
from .models import Picture


# Create your views here.
def pictures_view(request):
    return render(request, 'pictures.html')


def pictures_model_view(request):
    pictures = Picture.objects.all()
    return render(request, 'picture.html', {'objects': pictures})
