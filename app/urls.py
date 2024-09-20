from django.urls import path
from .views import home_view
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
    path("home/",home_view,name="home"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",logout_view, name="logout"),
]
