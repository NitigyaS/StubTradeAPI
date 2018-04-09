from django.conf.urls import url  , include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListView
from .views import CreateView
from .views import SymbolView


urlpatterns = {
    url(regex=r'^ticklist/all/$' ,view=ListView.as_view()),
    url(regex=r'^ticklist/(?P<symbol>\w{1,20})/$', view=SymbolView.as_view()),
    url(regex=r'tickadd/$' ,view=CreateView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)