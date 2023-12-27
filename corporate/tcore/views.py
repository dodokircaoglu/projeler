from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 return render(request, 'index.html')

def merhaba(request):
    # Görünüm fonksiyonu içinde işlemleri gerçekleştirin
    result = "Merhaba, Django!"

    # HttpResponse ile yanıt döndürme
    return HttpResponse(result)
def welcome_user(request):
    # Kullanıcı adını simüle etmek için bir bağlam (context) oluşturuyoruz
    user_name = "Bulut Kuru Php"

    # render fonksiyonu ile HTML şablonunu kullanarak bir HTTP yanıtı oluşturuyoruz
    return render(request, 'welcome_user.html', {'user_name': user_name})
