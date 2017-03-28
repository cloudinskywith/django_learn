### 1.第一章
pip3 install bpython --user

pip3 install virtualenv

virtualenv env_mysite

source env_mysite/bin/activate

pip install django==1.8.13

django-admin startproject mysite

```
django.contrib.admin – The admin site.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.
```

cd mysite
pymm
pyms

### 2.第二章 Views和URLconfs

- 在mysite先新建一个views.py
```
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello world'
```

- 在urls中关联views
```
from .views import hello

urlpatterns = [
    url(r'^admin',include(admin.site.urls)),
    url(r'hello',hello),
]
```

urlconf是松耦合的一个好例子


