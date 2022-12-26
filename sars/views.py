
from django.http import JsonResponse
import requests


def Home(request):

    URL = "https://api.covid19api.com/world/total"
    r = requests.get(url = URL)    
    data = r.json()
    # TODO: CACHING     
    return JsonResponse(data)


def Country(request):

    if request.GET.get('country') == None or request.GET.get('from') == None or request.GET.get('to') == None:
        data= {"error" : "True" , "Message" : "Missing Data"}
        return JsonResponse(data)
    

    country = request.GET['country']
    from_date =  request.GET['from']
    to_date = request.GET['to']
    PARAMS = {
        "from" : from_date,
        "to": to_date,  
    }
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
