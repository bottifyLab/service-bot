from orator import Model
from orator.orm import has_many
from orator.orm import belongs_to
from orator.orm import belongs_to_many
from orator.orm import scope
from orator.orm import accessor

from .connect import db

class Customer(Model):
  __guarded__ = ['created_at', 'updated_at']
  __visible__ = ['id', 'name', 'uid', 'wallet', 'banned', 'balance']

  @has_many
  def payments(self):
      return Payment

  @belongs_to_many
  def tickets(self):
      return Ticket

class Payment(Model):
    __guarded__ = ['created_at', 'updated_at']
    @belongs_to
    def customer(self):
        return Customer

class Ticket(Model):
    __guarded__ = ['created_at', 'updated_at']
    __visible__ = ['id', 'code', 'amount']
    @belongs_to_many
    def customers(self):
        return Customer

class Use(Model):
    __guarded__ = ['created_at', 'updated_at']
    __visible__ = ['customer_id', 'ticket_id']
    __table__ = 'customers_tickets'


