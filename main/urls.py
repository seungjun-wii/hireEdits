from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("opportunity", views.opport, name="opport"),
    path("profile", views.profile, name="profile"),
    path("profile/edit", views.edit, name="profile"),
    path("opportunity/company1", views.company1, name="company"),
    path("login", views.login, name="login")
]