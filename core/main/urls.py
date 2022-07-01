from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('<int:id>', views.HomeDetailView.as_view(), name='home_detail')
]