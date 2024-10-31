from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def np_release(requests):
    title = 'Выпуски'
    dates = ['15 января', '22 января', '29 января', '5 февраля']
    releases = [f'№{i} от {date}' for i, date in enumerate(dates, start=1)]
    context = {'title': title,
               'releases': releases}

    return render(requests, 'np_release.html', context=context)


def np_team(requests):
    title = 'Коллектив'
    team = {'Главный редактор': 'Иван Иванов',
            'Корректор': 'Пётр Петров',
            'Верстальщик': 'Марина Маринина',
            'Корреспондент': 'Елена Еленина'}
    context = {'title': title,
               'team': team}

    return render(requests, 'np_team.html', context=context)


def np_main(requests):
    return render(requests, 'np_main.html', context={'title': 'Главная страница'})
