from django.shortcuts import render

def mode(request):
    return render(request, "mode.html")


def database_mode(request):
    return render(request, "database_mode.html")
