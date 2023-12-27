from django import forms

from my_plants_CBV.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {"first_name": "First Name", "last_name": "Last Name"}


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {"first_name": "First Name", "last_name": "Last Name"}
