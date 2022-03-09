from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError


def custom_handler400(request, exception):
    return HttpResponseBadRequest('<h1>Неверный запрос!</h1>')


def custom_handler403(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещен!</h1>')


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>Такой страницы не существует!</h1>')


def custom_handler500(request):
    return HttpResponseServerError('<h1>Ошибка сервера!</h1>')
