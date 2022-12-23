
from django.http import JsonResponse
import requests


def Home(request):

    URL = "https://api.covid19api.com/world/total"
    r = requests.get(url = URL)    
    data = r.json()
    # TODO: CACHING     
    return JsonResponse(data)


def Country(request):
    country = 'jordan'
    PARAMS = {
        "from" : request.GET['from'],
        "to" :  request.GET['to']
    }
    print(PARAMS)
    URL = f"https://api.covid19api.com/country/{country}/status/confirmed"
    r = requests.get(url = URL , params= PARAMS)    
    data = r.json()   
    # TODO: CACHING  
    return JsonResponse(data , safe=False)

def All_Countries(request):

    URL = "https://api.covid19api.com/summary"
    r = requests.get(url = URL)    
    data = r.json() 
    # TODO: CACHING    
    return JsonResponse(data['Countries'] , safe=False)
