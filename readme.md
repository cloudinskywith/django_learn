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


### 3.第三章 模板引擎
Template,Context

一些流程控制和判断
```
{% if %}
{% else %}
{% elif %}
{% endif %}

{% for %}
{% endfor %}

{% for x, y in points %}
    There is a point at {{x}},{{y}}
{% endfor %}


{# This is a comment #}
```

- filter
```
{{ name | lower }}
{{ my_list | first | upper }}
{{ bio | truncatewords: "30" }}
{{ pub_date | date: "F j, Y" }}
//详见Appendix E
```

- include
```
{% include 'nav.html' %}
{% include 'include/nav.html' %}
```

- Inheritance

- 修改settings文件
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```







