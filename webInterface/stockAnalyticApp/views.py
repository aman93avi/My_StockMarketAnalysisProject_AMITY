# Create your views here.
from django.http import Http404

from django.shortcuts import render
import pymongo


conn = pymongo.MongoClient()
DB = conn["STOCK"]
stock_col = DB["stocks"]
exchange_col = DB["exchanges"]


def index(request):
    """ Index page
    :param request: request object
    :return: rendered index html page
    """
    return render(request , "home.html")



def exchange(request, NAME):
    """ Exchange detail
    :param request: request object
    :return: rendered  exchange html
    """
    res = exchange_col.find_one({"name":NAME})
    if res == None:
        raise Http404()
    else:
        response = {}
        response["name"] = res["name"]
        response["full_name"] = res["full_name"]
        response["desc"] = res["desc"]
        response["indices"] = res["indices"]

        return render(request, "exchange.html", response)



def company_detail(request):
    pass



