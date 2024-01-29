from django.urls import path
from . import views
from . import dataviews

app_name = "lyra"
urlpatterns = [
    # url: /lyra/
    path("", views.home, name="home"),
    path("data", views.mlproject, name="data"),
    path("gendata", dataviews.gen_data_view, name="gendata"),
    #path("showdata", dataviews.show_data, name="gendata")
]