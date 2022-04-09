import requests
from json import loads
from django.http import JsonResponse


def actiovation_post(request, uid, token):
    res = requests.post('http://127.0.0.1:8000/auth/users/activation/', data={"uid": uid, "token": token})
    if res.status_code == 204: return JsonResponse({"uid": "You have successfully verified your email"})
    else:
        return JsonResponse(loads(res.text))


