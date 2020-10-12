from django.conf.urls import url
from .views import MyLogoutView
from .views import RegistrationView
from .views import LoginUser

app_name = "accounts"

urlpatterns = [
    url(r'^login/$', LoginUser.as_view(), name="login"),
    url(r'^logout/$', MyLogoutView.as_view(), name="logout"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
]
