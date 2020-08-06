from django.conf.urls import url
# import views so we can use them in urls.
from . import views
from .views import AccueilView
from .views import ResultatsView
from .views import MoncompteView
from .views import CopyrightView
from .views import AlimentList
from .views import SearchProductView
from .views import SauvegardeView
#from django.contrib.auth.views import LoginView

app_name = "store"


urlpatterns = [
    url(r'^accueil/$', AccueilView.as_view(), name="accueil"),
    url(r'^resultats/$', ResultatsView.as_view(), name="resultats"),
    url(r'^aliment/$', AlimentList.as_view(),name="aliment"),
    url(r'^moncompte/$', MoncompteView.as_view(), name="moncompte"),
    #url(r'^register/$', views.registration, name='register'),
    #url('login/', LoginView.as_view(), name="login"),
    #url(r'^login/$', views.my_login, name="my_login"),
    url(r'^logout/$', views.logout_views, name="logout_views"),
    url(r'^search_product/$', SearchProductView.as_view(), name="search_product"),
    url(r'^sauvegarde/$', SauvegardeView.as_view(), name="sauvegarde"),
    url(r'^copyright/$', CopyrightView.as_view(), name="copyright"),
]
