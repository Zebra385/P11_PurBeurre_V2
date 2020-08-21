from django.conf.urls import url
# import views so we can use them in urls.
#from .views import LoginUser
from .views import LogoutView
from .views import RegistrationView
from .views import LoginUser

app_name = "accounts"

urlpatterns = [
    url(r'login/$', LoginUser.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
]
