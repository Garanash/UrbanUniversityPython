from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from task1.forms import ContactForm
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class GameAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer



def main_page(requests):
    return render(requests, 'main.html', context={'title': 'Главная страница'})


def games(request):
    posts = Game.objects.all().order_by('-size')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pagination.html', {'page_obj': page_obj, 'title': 'Игры'})


def games2(request):
    games_ = Game.objects.all().order_by('-size')
    items_per_page = request.GET.get('items_per_page', 5)
    paginator = Paginator(games_, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'items_per_page': items_per_page}
    return render(request, 'pagination2.html', context=context)


def cart(requests):
    title = 'Корзина'
    cart_ = 'Ваша корзина пуста'
    context = {'title': title,
               'cart': cart_}

    return render(requests, 'cart.html', context=context)


def sign_up(request):
    buyers = Buyer.objects.all()
    info = {}
    error = ''

    if request.method == 'POST':
        for key in ('username', 'balance', 'age'):
            info[key] = request.POST.get(key, '')

        if info['username'] not in [buyer.name for buyer in buyers]:
            Buyer.objects.create(name=info['username'],
                                 age=info['age'],
                                 balance=info['balance'])
        else:
            info['username'], username = None, info['username']
            error = f'Пользователь {username} уже зарегистрирован!'

    context = {'title': 'Регистрация', 'error': error, 'username': info.get('username')}
    return render(request, 'signup.html', context=context)


def games0(requests):
    games_ = Game.objects.all()
    title = 'Игры'
    context = {'title': title,
               'releases': games_,
               'games': games_}

    return render(requests, 'pagination.html', context=context)
