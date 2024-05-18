from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #index
    path('bestongoing/', views.bestongoingindex, name='bestongoing'),
    path('ongoing/', views.ongoingindex, name='ongoing'),
    path('upcoming/', views.upcomingindex, name='upcoming'),
    #en cartelera
    path('cartelera2/', views.ongoing, name='cartelera2'),
    path('cartelera/', views.ongoingrender, name='cartelera'),

    #soon
    path('proximo2/', views.upcoming, name='proximo2'),
    path('proximo/', views.upcomingrender, name='proximo'),

    #movie
    path('movie/<int:movie_id>/', views.movieview, name='movieview'),
]
