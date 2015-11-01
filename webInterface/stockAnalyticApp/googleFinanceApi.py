__author__ = 'vishnu'

import urllib2
import requests

SYMBOLS = {
    "bse": "INDEXBOM:SENSEX",
    "nse": "INDEXBOM"
}


# Constant
GOOG_API_URL = "http://finance.google.com/finance/info?client=ig&q="


def get_sensex_live():
    return requests.get(GOOG_API_URL, {'q': SYMBOLS['bse']})





