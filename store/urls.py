from django.conf.urls import url
from .views import AccueilView
from .views import MoncompteView
from .views import CopyrightView
from .views import SearchProductView

app_name = "store"

urlpatterns = [
    url(r'^accueil/$', AccueilView.as_view(), name="accueil"),
    url(r'^moncompte/$', MoncompteView.as_view(), name="moncompte"),
    url(r'^search_product/$',
        SearchProductView.as_view(),
        name="search_product"),
    url(r'^copyright/$', CopyrightView.as_view(), name="copyright"),
]
