from django.urls import include, path

from .views import Catalog, Home, Publications
from .views import Auth, User


app_name = 'getfashionable'
urlpatterns = [
    path('', Home.most_recent, name='home'),
    path("signup/", Auth.SignUp.as_view(), name="signup"),
    path("login/", Auth.SignIn.as_view(), name="login"),
    path("logout/", Auth.SignOut.as_view(), name="logout"),
    path('<int:id>/', Publications.publication_detail, name='publication_detail'),
    path('<str:username>/', User.Profile.as_view(), name="profile"),
]
