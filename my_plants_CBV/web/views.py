from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from my_plants_CBV.web.forms import CreateProfileForm, DeleteProfileForm
from my_plants_CBV.web.models import Plant, Profile


def get_profile():
    try:
        profile = Profile.objects.first()
        return profile
    except Exception:
        return None


class Index(view.TemplateView):
    template_name = 'home-page.html'
    profile = get_profile()
    if profile:
        have_profile = False
    else:
        have_profile = True

    extra_context = {"have_profile": have_profile}


class ProfileCreate(view.CreateView):
    form_class = CreateProfileForm
    profile = get_profile()
    if profile:
        have_profile = False
    else:
        have_profile = True

    extra_context = {"have_profile": have_profile}
    success_url = reverse_lazy('catalogue')
    template_name = 'create-profile.html'


class ProfileEdit(view.UpdateView):
    def get_object(self, *args, **kwargs):
        return Profile.objects.first()
    fields = "__all__"
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('profile_details')


class ProfileDelete(view.DeleteView, view.UpdateView):
    # model = Profile

    def get_object(self, *args, **kwargs):
        return Profile.objects.first()

    form_class = DeleteProfileForm
    Plant.objects.all().delete()
    template_name = 'delete-profile.html'
    success_url = reverse_lazy('home page')


class ProfileDetails(view.TemplateView):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    extra_context = {"profile": profile, "plants": plants}
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
    success_url = reverse_lazy('catalogue')
