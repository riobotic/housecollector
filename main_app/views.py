from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
   cat = Cat.objects.get(id=cat_id)
   return render(request, 'cats/detail.html', {'cat': cat })

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