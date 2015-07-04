from django.http import HttpResponse
from django.template import loader


def test(request):
    html = "<html><body>Hey that somehow worked!</body></html>"
    return HttpResponse(html)

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template)
