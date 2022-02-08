from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Link
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '') # gets the value of the site you've entered through the name of the site
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    #link_address = [] # To save in a list first

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)

        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
