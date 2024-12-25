from django.shortcuts import render


def home(request):
    """Функция-контроллер, рендерит шаблон страницы home"""

    return render(request, 'home.html')


def contacts(request):
    """Функция-контроллер, рендерит шаблон страницы contacts"""

    return render(request, 'contacts.html')