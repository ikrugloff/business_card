from django.shortcuts import render


# Create your views here.
def skills_view(request):
    tech_skills = ['Python 3+',
                   'Django 2+',
                   'HTML/CSS',
                   'SQL (Oracle SQL 11+, PostgreSQL 10+)',
                   'Linux OS (RedHat 7+, CentOS 7+)'
                   ]
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
    # my_skills = []  # To test if - else construction in skills.html
    return render(request, 'skills.html', {'tech_skills': tech_skills, 'finished_cources': finished_cources})
