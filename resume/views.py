from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from resume.models import Resume
# Create your views here.


def resume(request):
    resumes = Resume.objects.all()
    context = {'resumes': resumes}
    return render(request, 'resume.html', context=context)


class ResumeCreateView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            new_resume = Resume.objects.create(
                description=request.POST.get('description'),
                author=request.user
            )
            return redirect('/home')
        else:
            raise PermissionDenied
