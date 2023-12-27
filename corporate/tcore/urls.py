from django.urls import path
from .views import index,merhaba,welcome_user,deneme

urlpatterns =[
	path('', index, name='index'),
    path('merhaba/', merhaba, name='merhaba_view'),
    path('welcome/', welcome_user, name='welcome_user'),
    path('deneme/', deneme, name='deneme_view'),
]

