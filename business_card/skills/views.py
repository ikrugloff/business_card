from django.shortcuts import render
from .models import Skill, SkillRank


# Create your views here.
def skills_view(request):
    tech_skills = Skill.objects.all()
    finished_cources = ['Red Hat System Administration I (RH124, RedHat)',
                        'Red Hat System Administration II (RH134, RedHat)',
                        'Python. Level 1 (GeekBrains.ru)',
                        'Python. Level 2 (GeekBrains.ru)',
                        'Test automation introduction (GeekBrains.ru)',
                        'Database Basics (GeekBrains.ru)',
                        'Computer networks (GeekBrains.ru)',
                        'Git. Fast start (GeekBrains.ru)',
                        'Algorithms and data structures on Python. Basic course (GeekBrains.ru)',
                        'Product and project management (GeekBrains.ru)',
                        'Database Foundations (Oracle)',
                        'Introduction to Linux (stepik.org)',
                        'SQL for tester (software-testing.ru)'
                        ]
    # my_projects = [{'name': 'Business card', 'link': 'https://github.com/ikrugloff/business_card'}
    # ]
    # my_skills = []  # To test if - else construction in skills.html
    return render(request, 'skills.html', {'tech_skills': tech_skills, 'finished_cources': finished_cources})


def one_rank_view(request, rank_id):
    rank = SkillRank.objects.get(id=rank_id)
    skills = Skill.objects.filter(rank=rank)
    # skills = Skill.objects.filter(rank__id=rank_id)  # alter
    return render(request, 'rank.html', {'rank': rank, 'skills': skills})
