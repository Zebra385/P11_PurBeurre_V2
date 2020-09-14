from django.conf.urls import url
from .views import SauvegardeView
from .views import ResultatsView
from .views import AlimentListView

app_name = "substituts"

urlpatterns = [
    url(r'^resultats/$', ResultatsView.as_view(), name="resultats"),
    url(r'^sauvegarde/$', SauvegardeView.as_view(), name="sauvegarde"),
    url(r'^aliment/$', AlimentListView.as_view(), name="aliment"),
]
