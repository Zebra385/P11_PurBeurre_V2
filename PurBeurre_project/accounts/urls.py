from django.conf.urls import url
# import views so we can use them in urls.
from . import views
from .views import LoginView
from .views import LogoutView

#from django.contrib.auth.views import LoginView

app_name = "accounts"


urlpatterns = [
   
    #url(r'^register/$', views.registration, name='register'),
    url(r'login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    
]
