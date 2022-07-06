from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car, Category
# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cats = Category.objects.all()
        return render(request, self.template_name, {'cats':cats})

class CategoryListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        categorys = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'categorys':categorys})

class CategoryDetailView(DetailView):
    template_name = 'home_detail_detail.html'

    def get(self, request, id):
        car = Car.objects.get(pk=id)
        return render(request, self.template_name, {'car':car})

# class HomeDetailView(DetailView):
#     template_name = 'home_detail.html'

#     def get(self, request, id):
#         car = Car.objects.get(pk=id)
#         return render(request, self.template_name, {'car':car})

# class HomeMotoDetailView(DetailView):
#     template_name = 'home_detail_moto.html'

#     def get(self, request, test):
#         moto = Moto.objects.get(pk=test)
#         return render(request, self.template_name, {'moto':moto})