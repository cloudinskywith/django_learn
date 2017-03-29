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


### 5.第五章 admin
pym createsuperuser
liaobaocheng
917042364@qq.com
liaobaocheng

```
from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
```

### 6.第六章 forms
```
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your Email Address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not Enough Words!")
        return message


{% if form.errors %}
<p style="color: red;">
    please correct the error {{ form.errors | pluralize }} below
</p>
{% endif %}

<form action="" method="post">
    <table>
        {{form.as_table}}
    </table>
    {% csrf_token %}
    <input type="submit" value="subject">
</form>
</body>
</html>
```








