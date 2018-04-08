# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Generic Imports
from django.test import TestCase

# Imports for ModelTestCase
from .models import Ticks

# Imports for ViewTestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suits for the Ticks Models"""
    def setUp(self):
        self.symbol = "TCS"
        self.tcs_ticks = Ticks(symbol=self.symbol)
        pass
    def test_model_can_read_a_tick(self):
        symbol = self.tcs_ticks.symbol
        self.assertEqual(symbol,"TCS")


class ViewTestCase(TestCase):
    """This class defines the test suits for the Views"""
    def setUp(self):
        self.client = APIClient()
        self.response = self.client.get()

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Ticks.objects.get()
        response = self.client.get( format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)


