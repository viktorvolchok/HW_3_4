from django.http import HttpResponse


def books_view(request):
    return HttpResponse('{"name": "Кобзар"}')


def country_view(request):
    return HttpResponse('{"name": "Ukraine"}')
