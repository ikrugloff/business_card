from django.shortcuts import render


# Create your views here.
def skills_view(request):
    my_skills = ['Python 3+', 'Django 2+', 'Oracle SQL 11+', 'RedHat 7+']
    # my_skills = []  # To test if - else construction in skills.html
    return render(request, 'skills.html', {'my_skills': my_skills})
