from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from my_plants_CBV.web.forms import CreateProfileForm
from my_plants_CBV.web.models import Plant, Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    else:
        return None


class Index(view.TemplateView):
    template_name = 'home-page.html'
    no_profile = False
    if not get_profile():
        no_profile = True

    extra_context = {"no_profile": no_profile}


class ProfileCreate(view.CreateView):
    form_class = CreateProfileForm

    no_profile = False
    if not get_profile():
        no_profile = True

    extra_context = {"no_profile": no_profile}
    success_url = reverse_lazy('catalogue')
    template_name = 'create-profile.html'


class ProfileEdit(view.TemplateView):
    template_name = 'edit-profile.html'


class ProfileDelete(view.TemplateView):
    template_name = 'delete-profile.html'


class ProfileDetails(view.TemplateView):
    template_name = 'profile-details.html'


class Catalogue(view.ListView):
    queryset = Plant.objects.all()
    template_name = 'catalogue.html'


class PlantCreate(view.CreateView):
    model = Plant
    fields = "__all__"
    success_url = reverse_lazy('catalogue')
    template_name = "create-plant.html"



class PlantDetails(view.DetailView):
    model = Plant
    template_name = "plant-details.html"


class PlantEdit(view.UpdateView):
    model = Plant
    fields = "__all__"
    template_name = "edit-plant.html"
    success_url = reverse_lazy('catalogue')


class DeleteEdit(view.DeleteView):
    model = Plant
    template_name = "delete-plant.html"
