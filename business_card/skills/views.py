from django.shortcuts import render


# Create your views here.
def skills_view(request):
    return render(request, 'skills.html')
