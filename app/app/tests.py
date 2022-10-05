"""
Sample Tests
"""

from http import client
import unittest
from django.test import SimpleTestCase

from app import calc
from rest_framework.test import APIClient


class CalcTest(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

    def test_get_greeting(self):
        """Test Getting greetings"""
        client = APIClient()
        res = client.get("/greetings")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, "Hello")
