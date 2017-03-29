#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from books.models import Book
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


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


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    else:
        return render(request, 'search_form.html', {'errors': errors})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', '917042364@qq.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial={'subject': 'i love your site'}
        )
    return render(request, 'contact_form.html', {'form': form})

