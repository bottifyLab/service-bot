import random
import json
import requests
from time import sleep
from app.settings import *

public_key = settings.QIWI_P2P_PUBLIC
secret_key = settings.QIWI_P2P_SECRET

def get_secret_session():
    session = requests.Session()
    session.headers['Accept'] = 'application/json'
    session.headers['Content-Type'] = 'application/json'
    session.headers['authorization'] = 'Bearer ' + secret_key
    return session

def createBill(amount, billId, comment="Оплата тарифа в боте"):
    session = get_secret_session()
    parameters = { "amount": { "currency": "RUB", "value": int(amount)},
    "comment": comment,
    "expirationDateTime": "2022-12-02T09:02:00+03:00",
    "customFields" : {
    "themeCode": "Venyamyn-ChPi4jPOSMc",
    "yourParam1": "64728940", "yourParam2": "order 678"}}
    h = session.put('https://api.qiwi.com/partner/bill/v1/bills/' + billId, json = parameters)
    return h

def checkBill(billId):
    session = get_secret_session()
    h = session.get('https://api.qiwi.com/partner/bill/v1/bills/' + billId)
    return h.json()['status']['value']

def cancelBill(billId):
    session = get_secret_session()
    h = session.post('https://api.qiwi.com/partner/bill/v1/bills/' + billId + '/reject')
    return h.json()







