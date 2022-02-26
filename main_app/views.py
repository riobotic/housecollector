from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat, Toy
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
   cat = Cat.objects.get(id=cat_id)
   feeding_form = FeedingForm()
   return render(request, 'cats/detail.html', {
       'cat': cat, 
       'feeding_form': feeding_form 
    })

def add_feeding(request, cat_id):
    # 1) collect form input values
    form = FeedingForm(request.POST)
    # 2) valid input values
    if form.is_valid():
        # 3) save a copy of a new feeding instance in memory
        new_feeding = form.save(commit=False)
        # 4) attach a reference to the cat that owns the feeding
        new_feeding.cat_id = cat_id
        # 5) save the new feeding to the database
        new_feeding.save()
    # 6) redirect the user back to the detail
    return redirect('detail', cat_id=cat_id)

# Renders a template with a form on it
# Creates a model form based on the model
# Responds to GET and POST requests
#  1) GET render the new cat form
#  2) POST submit the form to create a new instance
# Validate form inputs
# Handles the necessary redirect following a model instance creating

class CatCreate(CreateView):
    model = Cat
    # fields = ('name', 'breed', 'age', 'description')
    fields = '__all__'
    # success_url = '/cats/' this will work, but it's not preferred
    # Fat Models, Skinny Controllers

class CatUpdate(UpdateView):
    model = Cat
    fields = ('name', 'breed', 'description', 'age')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')


class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'


class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'