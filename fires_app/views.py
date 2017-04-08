from django.shortcuts import render
from django.http import HttpResponseRedirect
from fires_app.form import NameForm, SatelliteForm, FireForm

def index(request):
    form = FireForm()
    return render(request, 'fires_app/index.html', {'form': form})
