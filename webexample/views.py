from django.http import HttpResponse


def basic_one(request):
    html="<html><body>ПРИВЕТ МИР! %s view</html></body>"
    return HttpResponse(html)

