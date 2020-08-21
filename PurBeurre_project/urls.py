"""PurBeurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import include,  path
from django.contrib import admin
from store.views import AccueilView


urlpatterns = [
    url(r'^$', AccueilView.as_view(), name="accueil"),
    # importation of the urls from app store
    url(r'^store/', include('store.urls')),
    #  importation of the url from app accounts
    url(r'^accounts/', include('accounts.urls')),
    #  importation of the url from app substituts
    url(r'^substituts/', include('substituts.urls')),
    url('admin/', admin.site.urls),
    path('store/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]
# Import toolbar to help to debug
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
