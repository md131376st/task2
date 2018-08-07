from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'task2'

urlpatterns = [
    url(r'1/$', views.MyView.as_view()),
    url(r'me/$',views.MyView1.as_view(), name="MyQuery")
]
urlpatterns = format_suffix_patterns(urlpatterns)


