from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="src"),
    path("newpage/", views.n_page, name="n_page"),
    path("edit/", views.edt, name="edit"),
    path("save_edt/", views.save_edt,name="save_edt"),
    path("ran/", views.ran, name="ran"),
    
]
