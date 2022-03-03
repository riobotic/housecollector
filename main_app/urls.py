from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='index'),
    path('houses/<int:house_id>/', views.houses_detail, name='detail'),
    path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
    path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='houses_update'),
    path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='houses_delete'),
    path('apartments/', views.ApartmentList.as_view(), name='apartments_index'),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view(), name='apartments_detail'),
    path('apartments/create/', views.ApartmentCreate.as_view(), name='apartments_create'),
    path('apartments/<int:pk>/update/', views.ApartmentUpdate.as_view(), name='apartments_update'),
    path('apartments/<int:pk>/delete/', views.ApartmentDelete.as_view(), name='apartments_delete'),   
]