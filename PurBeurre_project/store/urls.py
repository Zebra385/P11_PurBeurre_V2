from django.conf.urls import url

from . import views # import views so we can use them in urls.

app_name = "store"

urlpatterns = [
	url(r'^accueil/$', views.accueil, name="accueil"),
	url(r'^resultats/$', views.resultats, name="resultats"),
	url(r'^aliment/$', views.aliment, name="aliment"),
	url(r'^moncompte/$', views.moncompte, name="moncompte"),
	url(r'^register/$', views.registration, name='register'),
	#url(r'^login/$', views.login_views, name="login_views"),
	url(r'^logout/$', views.logout_views, name="logout_views"),
	url(r'^search_product/$', views.search_product, name="search_product"),
	url(r'^sauvegarde/$', views.sauvegarde, name="sauvegarde"),

    #url(r'^$', views.index), # "/store" will call the method "index" in "views.py"
]