#1/usr/bin/env python3.6

from password import User
from password import Credentilas
from random import randint #enables use of randit method to import random string

def new_user(username, password):
  """
  creates a new user
  """
  
  return User(username, password)
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
def save_account(password):
  """
  saving account details
  """
  password.save_account()
def delete_accounts(password):
  """
  deleting account details
  """
  password.delete_accounts()
def display_account_details():
  """
  displays saved account details
  """
  return Credentilas.display_account()
  
  
def main():
  """
  main functions called here
  """"
  print("--------------------------- ")
  print("--------------------------- ")
  print("--PASSWORD LOCCKER APP :)--")
  
  print(":) :) :) :) :) :)")
  print("CREATE A PASSWORD LOCKER ACCOUNT FIRST!!")
  print("--------------------------- ")
  print("--------------------------- ")
  
  
  