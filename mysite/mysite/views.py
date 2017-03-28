#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse('hello world')


def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    return render(request, 'sub/current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hours,it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


