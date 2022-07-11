from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('brands/<str:id>', views.BrandListView.as_view(), name='brands'),
    path('category/<str:id>', views.CategoryListView.as_view(), name='home_detail'),
    path('category/car/<int:id>', views.CategoryDetailView.as_view(), name='home_detail_detail'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name = 'logout'),

]