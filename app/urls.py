from django.urls import path
from .views import home_view
from django.contrib.auth import views as auth_views
from .views import logout_view, add_declaration, declaration_success_view

urlpatterns = [
    path("home/",home_view,name="home"),
    path("accounts/login/",auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",logout_view, name="logout"),
    path("add-declaration/",add_declaration, name="add-declaration"),
    path("declaration-success/", declaration_success_view, name="declaration-success"),
]
