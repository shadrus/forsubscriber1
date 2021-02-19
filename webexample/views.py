from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template


def basic_one(request):
    html = "<html><body>ПРИВЕТ МИР! %s view</html></body>"
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render({'name': view})

    return HttpResponse(html)


def template_three(request):
    view = "template_three"
    return render(request, 'myview.html', {'name': view})
