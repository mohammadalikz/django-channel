from django.urls import path
from echo import views
urlpatterns = [
    path('' , views.index , name = 'index'),
]