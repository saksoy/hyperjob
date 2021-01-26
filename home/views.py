from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from .forms import HomeForm
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        is_staff = request.user.is_staff
        form = HomeForm()
        context = {'is_staff': is_staff, 'form': form}
        return render(request, 'home.html', context=context)
