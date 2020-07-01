from django.conf.urls import url

from . import views # import views so we can use them in urls.

app_name = "store"

urlpatterns = [
	url(r'^accueil/$', views.accueil, name="accueil"),
	url(r'^resultats/$', views.resultats, name="resultats"),
	url(r'^aliment/$', views.aliment, name="aliment"),
	url(r'^moncompte/$', views.moncompte, name="moncompte"),
	#url(r'^affichage_base/$', views.affichage_base, name="affichage_base"),
	#url(r'^affichage_base_product/$', views.affichage_base_product, name="affichage_base_product"),

    #url(r'^$', views.index), # "/store" will call the method "index" in "views.py"
]