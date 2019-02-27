from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cocktails", views.cocktails, name="cocktails"),
    path("details/<int:drink>", views.details, name="details"),
    path("home/<str:lastPage>/", views.home, name="home"),
    path("page2/<str:lastPage>/", views.page2, name="page2"),
    path("page3/<str:lastPage>/", views.page3, name="page3"),
    path("page4/<str:lastPage>/", views.page4, name="page4"),
    path("page5/<str:lastPage>/", views.page5, name="page5"),
]





