from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    url(r'^members/$', views.MemberList.as_view(), name='members'),
    url(r'^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    url(r'^interests/$', views.InterestList.as_view()),
    url(r'^interests/(?P<pk>[0-9]+)/$', views.InterestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
