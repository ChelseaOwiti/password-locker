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

  
  

  