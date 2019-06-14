import unittest
from password import User
from password import Credentilas

class TestUser(unittest.TestCase):
  """
  Test class that defines  test cases for user class
  """
  def setUp(self):
    """
    method to run before each test
    """
    self.new_user = User("Chelsea", "12345")
  def tearDown(self):
    User.user_list = []
    
  def test_init(self):
    self.assertEqual(self.new_user.username, "Chelsea")
    self.assertEqual(self.new_user.password, "12345")
      
      
if __name__ == '__main__':
  unittest.main()