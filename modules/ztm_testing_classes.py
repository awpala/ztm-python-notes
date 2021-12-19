import unittest
from modules.ztm_testing_functions import do_stuff 

# reference docs for `unittest`: https://docs.python.org/3/library/unittest.html


class TestDoStuff(unittest.TestCase):
  def SetUp(self):
    pass # set up before each test here

  def test_do_stuff_int(self):
    test_param = 10
    result = do_stuff(test_param)
    self.assertEqual(result, 15)
  
  def test_do_stuff_default(self):
    result = do_stuff()
    self.assertEqual(result, 5)

  def test_do_stuff_str(self):
    test_param = 'shkshks'
    result = do_stuff(test_param)
    self.assertIsInstance(result, TypeError)

  def test_do_stuff_none(self):
    test_param = None
    result = do_stuff(test_param)
    self.assertIsInstance(result, TypeError)

  def tearDown(self):
    pass # tear down / clean up, reset, etc. after each test here
