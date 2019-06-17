#1/usr/bin/env python3.6

from password import User
from password import Credentilas
from random import randint #enables use of randit method to import random string

def new_user(username, passwords):
  """
  creates a new user
  """
  new_user = User(username, passwords)
  return new_user
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
  print("What is your name?")
  
  user_name = input()
  print("--------------------------- ")
  print("--------------------------- ")
  
  print(f"Hey {user_name}. Would you like to create an account?")
  print("\n")
  
  while True:
    print("Use these codes to make requests:")
    print("us- add user account")
    print("ca- create an account")
    print("da - delete and account")
    print("va- view account details")
    
    short_code = input().lower()
    
    if short_code == "us":
    print("USER ACCOUNT")
    print ("Enter username")
    username = input()
    
    print ("Enter NEW USER password")
    passwords = input()
    
    save_user(new_user(username, passwords))
    
    print("User account {username} created")
        
   
  