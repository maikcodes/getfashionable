from django.urls import include, path

from .views import Home, Publications
from .views import Profile
from .views.Auth import SignUp, SignIn, SignOut
from .views.Design import CreateDesign


app_name = 'getfashionable'
urlpatterns = [
    path('', Home.most_recent, name='home'),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", SignIn.as_view(), name="login"),
    path("logout/", SignOut.as_view(), name="logout"),
    path('designs/', CreateDesign.as_view(), name="designs"),
    path('<int:id>/', Publications.publication_detail, name='publication_detail'),
    path('<str:username>/', Profile.as_view(), name="profile"),
]
