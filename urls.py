from django.urls import path
from . import views


urlpatterns = [
      path("", views.home, name="home"),
      path("about", views.about, name="about"),
      path("contact", views.contact, name="contact"),
      path("search", views.search, name="search"),
      path("signup", views.sign_up, name="signup"),
      path("login", views.user_login, name="login"),
      path("logout", views.user_logout, name="logout")

]
