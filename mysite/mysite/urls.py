from django.conf.urls import include, url
from django.contrib import admin
from .views import hello, current_datetime, hours_ahead

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]
