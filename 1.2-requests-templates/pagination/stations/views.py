from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))
 

def bus_stations(request):
    with open('/Users/antonarambillet/Desktop/Django/Echeverria_Anton_DJ-66/1.2-requests-templates/pagination/data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = [row for row in reader]

        num_page = request.GET.get('page')
        paginator = Paginator(bus_stations, 10)
        page = paginator.get_page(num_page)

    context = {
         'bus_stations': page,
         'page': page
    }
    return render(request, 'stations/index.html', context)