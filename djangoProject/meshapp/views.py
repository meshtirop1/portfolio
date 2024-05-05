from django.shortcuts import render

from meshapp.models import Project, GalleryImage


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def education(request):
    return render(request, 'education.html')


def projects(request):
    context = {
        'incomplete_projects': [],
        'complete_projects': [],
    }
    return render(request, 'projects.html', context)


def contact(request):
    return render(request, 'contact.html')


def web(request):
    return render(request, 'web.html')


def math(request):
    return render(request, 'math.html')


# def securitty(request):
#     return render(request, 'cybersecurity.html')


def cybersecurity(request):
    return render(request, 'cybersecurity.html')


def django(request):
    return render(request, 'django.html')


def rongo(request):
    return render(request, 'rongo.html')


def kdu(request):
    return render(request, 'kdu.html')


# def pictures(request):
#     return render(request, 'gallery.html')
#
def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})


def completed_projects(request):
    projects = Project.objects.filter(status='completed').order_by('-created_at')
    context = {'projects': projects, 'title': 'Completed Projects'}
    return render(request, 'completed.html', context)


def incomplete_projects(request):
    projects = Project.objects.filter(status='incomplete').order_by('-created_at')
    context = {'projects': projects, 'title': 'Incomplete Projects'}
    return render(request, 'incomplete.html', context)


def school_projects(request):
    projects = Project.objects.filter(status='school').order_by('-created_at')
    context = {'projects': projects, 'title': 'School Projects'}
    return render(request, 'mandatory.html', context)
