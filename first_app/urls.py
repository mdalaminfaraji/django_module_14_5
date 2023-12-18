from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('form', views.submit_form, name="submit_form"),
    path('about', views.about, name="about"),
    path('practice_form', views.DjangoForm, name="practice_form"),
    path('geekForGeek', views.geekForm, name="geekForGeek")
]
