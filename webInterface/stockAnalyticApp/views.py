# Create your views here.
from django.shortcuts import render



def index(request):
    """
    :param request: request object
    :return: rendered index html page
    """
    return render(request , "home.html")


def company_detail(request):
    pass



