from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_link, name="create_link"),
    path("show_link/", views.show_link, name="show_link"),
    path("shortlink/<str:short_code>/", views.redirect_short_link, name="redirect_short_link"),
]