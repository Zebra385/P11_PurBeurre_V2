from django.conf.urls import url
# import views so we can use them in urls.
from . import views
from .views import AccueilView

from .views import MoncompteView
from .views import CopyrightView

from .views import SearchProductView

#from django.contrib.auth.views import LoginView

app_name = "store"


urlpatterns = [
    url(r'^accueil/$', AccueilView.as_view(), name="accueil"),
    
   
    url(r'^moncompte/$', MoncompteView.as_view(), name="moncompte"),
    url(r'^search_product/$', SearchProductView.as_view(), name="search_product"),
    url(r'^copyright/$', CopyrightView.as_view(), name="copyright"),
]
