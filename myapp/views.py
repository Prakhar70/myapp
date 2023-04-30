from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Index<h1>")

def about(request):
    return HttpResponse("<h1>About<h1>")

def service(request):
    return HttpResponse("<h1>Service<h1>")
