from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
