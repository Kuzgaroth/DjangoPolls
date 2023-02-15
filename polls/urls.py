from django.urls import include, re_path

from . import views
from .views import QuestionDetailView

app_name = 'polls'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    re_path(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail')
]
