from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from .models import Trip, Notes
# Create your views here.

def trips_view(request):
    trips = Trip.objects.all()
    context = {
        'trips' : trips,
    }
    return render(request, 'trip/trip_list.html', context)

def trips_specific_view(request,pk):
    trips = get_object_or_404(Trip,pk=pk)
    context = {
        'trips' : trips,
    }
    return render(request, 'trip/trip_list.html', context)

def note_view(request):
    notes = Notes.objects.all()
    context = {
        'notes' : notes,
    }
    return render(request, 'trip/note_list.html', context)

def note_specific_view(request,pk):
    notes = Notes.objects.filter(pk=pk).first()
    context = {
        'notes' : notes,
    }
    return render(request, 'trip/note_specific_list.html', context)

class CreateTrip(CreateView):
    model = Trip
    success_url = reverse_lazy("trips-view")
    fields = ["city","country","start_date","end_date"]
    
    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)