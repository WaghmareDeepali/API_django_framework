from django.http import HttpResponse,JsonResponse

def home(request):
    print("HELLO home function..")
    friends=['ankit','rupali','deepali']
    return JsonResponse(friends,safe=False)