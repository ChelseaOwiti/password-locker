class User:
  """
  class containing user details
  """
  user_list = [] #empty login list
  def __init__(self, username, password):
    """
    creates unique details for each instance
    """
    self.username = username
    self.password = password
    
    
    
    
class Credentilas:
  """
  class containing account details
  """
  account_list = [] #empty account list
  def __init__(self, sitename, accountname, password):
    """
    Creates unique details for credentials
    """
    self.sitename = sitename
    self.accountname = accountname
    self.password = password
  
  def save_account(self):
    Credentilas.account_list.append(self)
    
  def delete_account(self):
    Credentilas.account_list.remove(self)  
  