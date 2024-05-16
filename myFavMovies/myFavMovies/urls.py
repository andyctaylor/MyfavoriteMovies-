from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Using the names instead of the url for the dynamic django template
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
]
