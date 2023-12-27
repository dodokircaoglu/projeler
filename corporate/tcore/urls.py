from django.urls import path
from .views import index,merhaba,welcome_user

urlpatterns =[
	path('', index, name='index'),
    path('merhaba/', merhaba, name='merhaba_view'),
    path('welcome/', welcome_user, name='welcome_user'),
]

