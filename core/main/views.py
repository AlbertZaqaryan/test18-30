from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car
# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars':cars})



class HomeDetailView(DetailView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        car = Car.objects.get(pk=id)
        return render(request, self.template_name, {'car':car})
