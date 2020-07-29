from django.conf.urls import url
# import views so we can use them in urls.
from . import views

app_name = "store"

urlpatterns = [
    url(r'^accueil/$', views.accueil, name="accueil"),
    url(r'^resultats/$', views.resultats, name="resultats"),
    url(r'^aliment/$', views.aliment, name="aliment"),
    url(r'^moncompte/$', views.moncompte, name="moncompte"),
    url(r'^register/$', views.registration, name='register'),
    url(r'^logout/$', views.logout_views, name="logout_views"),
    url(r'^search_product/$', views.search_product, name="search_product"),
    url(r'^sauvegarde/$', views.sauvegarde, name="sauvegarde"),
    url(r'^copyright/$', views.copyright, name="copyright"),
]
