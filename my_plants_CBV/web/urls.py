from django.urls import path, include

from my_plants_CBV.web.views import Index, ProfileCreate, ProfileDetails, ProfileEdit, ProfileDelete, Catalogue, \
    PlantCreate, PlantDetails, PlantEdit, DeleteEdit

urlpatterns = [
    path('', Index.as_view(), name='home page'),
    path('catalogue/', Catalogue.as_view(), name='catalogue'),
    path('create/', PlantCreate.as_view(), name='plant_create'),
    path('details/<int:pk>', PlantDetails.as_view(), name='plant_details'),
    path('edit/<int:pk>', PlantEdit.as_view(), name='plant_edit'),
    path('delete/<int:pk>', DeleteEdit.as_view(), name='plant_delete'),


    path('profile/', include([
        path('create/', ProfileCreate.as_view(), name='profile_create'),
        path('detasils/', ProfileDetails.as_view(), name='profile_details'),
        path('edit/', ProfileEdit.as_view(), name='profile_edit'),
        path('delete/', ProfileDelete.as_view(), name='profile_delete'),
        ])),

]
