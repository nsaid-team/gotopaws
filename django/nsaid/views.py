from django.http import HttpResponse
from django.template import loader


def test(request):
    html = "<html><body>Hey that somehow worked!</body></html>"
    return HttpResponse(html)

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def shelters(request):
    template = loader.get_template('Shelters.html')
    return HttpResponse(template.render())

def pets(request):
    template = loader.get_template('Pets.html')
    return HttpResponse(template.render())

def cities(request):
    template = loader.get_template('Cities.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def cats(request):
    template = loader.get_template('Cats.html')
    return HttpResponse(template.render())

def dogs(request):
    template = loader.get_template('Dogs.html')
    return HttpResponse(template.render())

def shelter_apa(request):
    template = loader.get_template('Shelter_APA.html')]
    return HttpResponse(template.render())
