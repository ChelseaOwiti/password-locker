#1/usr/bin/env python3.6

from password import User
from password import Credentilas
from random import randint #enables use of randit method to import random string

def new_user(username, password):
  """
  creates a new user
  """
  new_user = User(username, password)
  return new_user(password)
def save_user(user):
  """
  save created user
  """
  user.save_user()
def create_account(sitename, accountname, password):
  """
  creating account details
  """
  new_account = Credentilas(sitename, accountname, password):
  return new_account
def save_account(account):
  """
  saving account details
  """
  account.save_account()
  
  

  