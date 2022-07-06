from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('category/<str:id>', views.CategoryListView.as_view(), name='home_detail'),
    path('category/car/<int:id>', views.CategoryDetailView.as_view(), name='home_detail_detail')
    # path('<int:test>', views.HomeMotoDetailView.as_view(), name='home_detail_moto'),

]