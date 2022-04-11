# from SimpleQIWI import *
import random
import json
import requests
from time import sleep
from app.settings import *

cf_token = settings.QIWI_TOKEN

# Сессия для запросов к API
def get_session():
    session = requests.Session()
    session.headers['Accept']= 'application/json'
    session.headers['authorization'] = 'Bearer ' + cf_token
    return session

# Профиль пользователя
def get_profile():
    session = get_session()
    p = session.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    return p.json()

# Телефон аккаунта
def get_phone():
    profile = get_profile()
    return str(profile['contractInfo']['contractId'])

# Никнейм аккаунта
def get_nickname():
    phone = get_phone()
    session = get_session()
    p = session.get('https://edge.qiwi.com/qw-nicknames/v1/persons/' + phone + '/nickname')
    return p.json()['nickname']

# Создание формы на оплату по никнейму
def create_form(comment):
  nickname = get_nickname()
  session = get_session()
  parameters = {
                #'extra[\'account\']': cf_phone,
                'extra[\'accountType\']': 'nickname',
                'extra[\'account\']': nickname,
                'extra[\'comment\']': f'{comment}',
                'amountFraction':'0',
                'currency': '643',
                #'amount': amount,
                'blocked[0]': 'account',
                'blocked[1]': 'comment',
                #'blocked[2]': 'sum',
                'blocked[3]': 'accountType'
                }
  h = session.get('https://qiwi.com/payment/form/99999?', params = parameters)
  return h.url

# История платежей - последние и следующие n платежей
def payment_history_last(rows=50):
    phone = get_phone()
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + cf_token
    parameters = {'rows': rows, 'operation': 'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + phone + '/payments', params = parameters)
    data = h.json()['data']
    payments_dict = {}
    for payment in data:
        amount = payment['sum']['amount']
        comment = payment['comment']
        new_dict = {comment:amount}
        payments_dict.update(new_dict)
    return payments_dict


# Проверка платежа с указанным комментарием
def check_payment_comment(comment):
  payments = payment_history_last()
  if comment in payments:
    return payments[comment]
  else:
    return False

# Рандомный комент
def gen_comment():
  number = random.randint(100000000,500000000)
  generate_comment = str(number)
  return generate_comment

# Проверка баланса
def check_balance():
  phone = get_phone()
  session = get_session()
  p = session.get('https://edge.qiwi.com/funding-sources/v2/persons/' + phone + '/accounts')
  return float(p.json()['accounts'][0]['balance']['amount'])
