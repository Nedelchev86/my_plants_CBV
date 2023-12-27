from django.contrib import admin

from my_plants_CBV.web.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Plant)
class AdminPlants(admin.ModelAdmin):
    pass

