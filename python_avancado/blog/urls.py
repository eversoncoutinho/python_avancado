from django.urls import path
from .views import home #importe a função necessãria

urlpatterns = [
    path('urlfilho/', home, name='home'), #agora tem que ir na pasta urls.py geral
]
