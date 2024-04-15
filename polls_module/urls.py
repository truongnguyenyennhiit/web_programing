from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  ## path trống thì gọi hàm index
    path("about", views.about, name="about"), 
    path("privacy", views.privacy, name="privacy"),
    path("hello/<int:number>/", views.hello, name="hello"),
    path("render", views.render123, name="render")
]