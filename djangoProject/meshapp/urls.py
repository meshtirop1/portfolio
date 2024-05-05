
from django.urls import path

from .views import (
    home,
    about,
    education,
    projects,
    contact,
    web,
    math,
    cybersecurity,
    django,
    rongo,
    kdu,
    completed_projects,
    incomplete_projects,
    school_projects,
    gallery,

)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('education/', education, name='education'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('web/', web, name='web'),
    path('math/', math, name='math'),
    path('cybersecurity/', cybersecurity, name='cybersecurity'),
    path('django/', django, name='django'),
    path('rongo/', rongo, name='rongo'),
    path('kdu/', kdu, name='kdu'),
    path('projects/completed/', completed_projects, name='completed_projects'),
    path('projects/incomplete/', incomplete_projects, name='incomplete_projects'),
    path('projects/school/', school_projects, name='school_projects'),
    path('gallery/', gallery, name='gallery')
]
