from django.shortcuts import render
from .models import Profile, Skill, Project, Experience, Education, Certification

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-year')
    certifications = Certification.objects.all().order_by('-date')
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
    }
    return render(request, 'portfolio/home.html', context)
