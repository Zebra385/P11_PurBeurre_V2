from django.conf.urls import url
# import views so we can use them in urls.
from .views import LoginView
from .views import LogoutView
from .views import RegistrationView
from .views import InscriptionView
app_name = "accounts"

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^inscription/$', InscriptionView.as_view(), name="inscription")
]
