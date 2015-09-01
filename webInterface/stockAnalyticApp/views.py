from django.shortcuts import render

# Create your views here.

def index(request):
    """
    :param request: request object
    :return: rendered index html page
    """
    return render(request ,"index.html")