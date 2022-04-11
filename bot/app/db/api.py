from .models import *
from app.settings import *

def getInformation():
    customers_count = Customer.all().count()
    return f"<b>👥 Пользователей в боте:</b> {customers_count}"

def findUser(uid):
    user = Customer.where('uid', str(uid)).first()
    return user

def registerUser(uid,name):
    customer = Customer.where('uid', str(uid)).first()
    if customer:
        return customer.serialize()
    else:
        customer = Customer.create(
            uid=uid,
            name=name,
            balance=0)
        return f"success registration customer with {customer.uid}"

def getCustomers(banned=0):
    customers = Customer.where('banned', banned).get().serialize()
    return customers

def getCustomer(customer_id):
  q = Customer.find(customer_id).serialize()
  return q

def banCustomer(customer_id):
    q = Customer.find(customer_id)
    return q.ban()

def updateCustomer(customer_id: int, params):
    customer = Customer.find(customer_id)
    if customer:
        customer.update(params)
        return customer.serialize()
    else:
        return "customer not found"

def makePayment(customer_id, amount, provider, comment):
    payment = Payment.create(customer_id=customer_id, amount=amount, provider=provider, comment=comment)
    return payment.serialize()

def confirmPayment(payment_id):
    payment = Payment.find(payment_id)
    if payment.confirmed:
        return "Платеж уже проведене"
    else:
        payment.confirmed=1
        payment.save()
        customer = payment.customer
        customer.balance += payment.amount
        customer.save()
        return f"Платеж на сумму {payment.amount} успешно зачислен!"

def makeTicket(code,amount):
    ticket = Ticket.create(code=code, amount=amount)
    return ticket.serialize()






