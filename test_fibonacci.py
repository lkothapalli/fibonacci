# -*- coding: utf-8 -*-
from flask import Flask
import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):


   def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
           
            
   def test_fibpositive(self):
            response = fibonacci(5)
            self.assertEqual(response.status_code,200)

   def test_fibnegative(self):
            response = fibonacci(-5)
            self.assertEqual(response,"Please enter a positive integer")

            

            
if __name__ == '__main__' : 
    unittest.main()