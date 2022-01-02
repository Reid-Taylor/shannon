from django.urls import path
from dmdd_pictures import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/<id>", views.showPicture, name="ident"),
    path("api", views.log_message, name="api")
    # path('load', views.loadData,name="loader")
]