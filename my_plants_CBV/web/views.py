from django.shortcuts import render
from django.views import generic as view

from my_plants_CBV.web.models import Plant


# Create your views here.


class Index(view.TemplateView):
    template_name = 'home-page.html'


class ProfileCreate(view.TemplateView):
    template_name = 'create-profile.html'


class ProfileEdit(view.TemplateView):
    template_name = 'edit-profile.html'


class ProfileDelete(view.TemplateView):
    template_name = 'delete-profile.html'


class ProfileDetails(view.TemplateView):
    template_name = 'profile-details.html'


class Catalogue(view.TemplateView):
    pass


class PlantCreate(view.CreateView):
    model = Plant
    fields = "__all__"
    template_name = "create-plant.html"


class PlantDetails(view.DetailView):
    model = Plant
    template_name = "plant-details.html"


class PlantEdit(view.UpdateView):
    model = Plant
    template_name = "edit-plant.html"


class DeleteEdit(view.DeleteView):
    model = Plant
    template_name = "delete-plant.html"
