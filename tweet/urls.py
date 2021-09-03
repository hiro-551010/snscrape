from django.urls import path, include
from tweet import views

app_name = "twitter"

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search, name="search"),
]