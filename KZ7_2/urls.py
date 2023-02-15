from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^polls/', include('polls.urls')),
    re_path(r'^admin/', admin.site.urls)
]
