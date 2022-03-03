from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import House, Apartment

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', {'houses': houses})

def houses_detail(request, house_id):
   house = House.objects.get(id=house_id)
   return render(request, 'houses/detail.html', {
       'house': house,     })

class HouseCreate(CreateView):
    model = House
    fields = '__all__'


class HouseUpdate(UpdateView):
    model = House
    fields = ('name', 'location', 'description', 'price')

class HouseDelete(DeleteView):
    model = House
    success_url = '/houses/'

class ApartmentCreate(CreateView):
    model = Apartment
    fields = ('name', 'location')


class ApartmentUpdate(UpdateView):
    model = Apartment
    fields = ('name', 'location')


class ApartmentDelete(DeleteView):
    model = Apartment
    success_url = '/apartments/'


class ApartmentDetail(DetailView):
    model = Apartment
    template_name = 'apartments/detail.html'


class ApartmentList(ListView):
    model = Apartment
    template_name = 'apartments/index.html'