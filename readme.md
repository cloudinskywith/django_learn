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

### 4.第四章 模型
python manage.py startapp books


更详细的field类型详见Appendix B
```
// models.py
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
```

- 1.pym check #检查系统
- 2.在settings中增加app
- 3.pym makemigratons books #生成migrate
- 4.pym sqlmigrate books 0001 #查看sql语法
- 5.pym migrate



