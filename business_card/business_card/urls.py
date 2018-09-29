"""business_card URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # NB! Use include in prod projects
from main_page.views import main_page_view
from about.views import about_view
from skills.views import skills_view, one_rank_view
from contacts.views import contacts_view
from pictures.views import pictures_view

urlpatterns = [
    # path('business_card/', include('business_card.urls')),  # TODO: necessary to explain include()
    path('admin/', admin.site.urls),
    path('', main_page_view, name='index'),
    path('about/', about_view, name='about'),
    path('skills/', skills_view, name='skills'),
    path('skills/rank/<int:rank_id>/', one_rank_view, name='rank'),
    path('contacts/', contacts_view, name='contacts'),
    path('pictures/', pictures_view, name='pictures')
]
