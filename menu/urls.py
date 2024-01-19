from django.urls import path

from . import views
from .views import MenuView

app_name='menu'
urlpatterns = [
    path("",  MenuView.as_view(), name="menu"),
]
