from django.urls import path
from . import views

app_name = "lyra"
urlpatterns = [
    # url: /lyra/
    path("", views.home, name="home"),
]