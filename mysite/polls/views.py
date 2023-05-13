from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellooooo, world. You're at the polls index.")