from django.urls import path, include
from .views import trips_view, note_view, note_specific_view, CreateTrip
urlpatterns = [
    path("", trips_view, name ='trips-view'),
    path("notes/", note_view, name = 'note-view'),
    path("notes/<int:pk>/", note_specific_view, name = 'note-spe-view'),
    path("trip/create/", CreateTrip.as_view(), name = 'create-trip')
]   
