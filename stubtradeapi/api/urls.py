from django.conf.urls import url  , include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListView
from .views import CreateView

urlpatterns = {
    url(regex=r'ticklist/$' ,view=ListView.as_view(), kwargs=None , name="list"),
    url(regex=r'tickadd/$' ,view=CreateView.as_view(), kwargs=None , name="add"),
}

urlpatterns = format_suffix_patterns(urlpatterns)