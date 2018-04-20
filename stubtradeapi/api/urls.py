from django.conf.urls import url  , include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListView
from .views import CreateView
from .views import SymbolView
from .views import ExactSymbolView
from rest_framework.documentation import include_docs_urls


urlpatterns = {
    url(r'^docs/', include_docs_urls(title='StubTradeAPI Documentation')),
    url(regex=r'^ticklist/all/$' ,view=ListView.as_view()),
    url(regex=r'^ticklist/(?P<symbol>\w{1,20})/(?P<range>\d+\w+)/$', view=SymbolView.as_view()),
    url(regex=r'^ticklist/(?P<symbol>\w{1,20})/exact/(?P<range>\d+\w+)/$', view=ExactSymbolView.as_view()),
    url(regex=r'tickadd/$' ,view=CreateView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)