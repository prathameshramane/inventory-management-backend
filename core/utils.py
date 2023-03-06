from django.conf import settings
from decouple import config
import requests


def getData(request):
    data = {}

    if request.data.get('name', None) is not None:
        data['name'] = request.data.get('name', None)
    if request.data.get('factory', None) is not None:
        data['factory_id'] = request.data.get('factory', None)
    if request.data.get('quantity', None) is not None:
        data['quantity'] = request.data.get('quantity', None)

    return data


def addNewProduct(request):
    req = requests.post(
        f'{settings.APIM_BASE}/prathamesh/orders/products/details/',
        data=getData(request),
        headers={'Ocp-Apim-Subscription-Key': config('APIM_KEY')})
    return req.status_code


def updateProduct(request, id):
    req = requests.patch(
        f'{settings.APIM_BASE}/prathamesh/orders/products/details/{id}/',
        data=getData(request),
        headers={'Ocp-Apim-Subscription-Key': config('APIM_KEY')})
    return req.status_code


def deleteProduct(id):
    req = requests.delete(
        f'{settings.APIM_BASE}/prathamesh/orders/products/details/{id}/',
        headers={'Ocp-Apim-Subscription-Key': config('APIM_KEY')})
    return req.status_code
