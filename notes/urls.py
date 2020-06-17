from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('chemistry', views.chem, name="chemistry"),
    path('botany', views.bot, name="botany"),
    path('zoology', views.zoo, name="zoology"),
    path('sem_1', views.semister1, name="sem_1"),
    path('sem_2', views.semister2, name="sem_2"),
    path('sem_3', views.semister3, name="sem_3"),
    path('sem_4', views.semister4, name="sem_4"),
    path('sem_5', views.semister5, name="sem_5"),
    path('sem_6', views.semister6, name="sem_6"),

]
