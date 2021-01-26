from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from vacancy.models import Vacancy
# Create your views here.


def vacancy(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy.html', context=context)


class VacancyCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            new_vacancy = Vacancy.objects.create(
                description=request.POST.get('description'),
                author=request.user
            )
            return redirect('/home')
        else:
            raise PermissionDenied
