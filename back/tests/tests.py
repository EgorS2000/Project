from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class RegistrationTestCase(APITestCase):
    def test_registration_201(self):
        data = {
            'username': 'egor',
            'password': 'egor12345678',
            're_password': 'egor12345678'
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_400_1(self):
        data = {
            'username': '',
            'password': 'egor12345678',
            're_password': 'egor12345678'
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_400_2(self):
        data = {
            'username': 'egor',
            'password': '',
            're_password': ''
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_400_3(self):
        data = {
            'username': 'egor',
            'password': 'egor12345678',
            're_password': ''
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_400_4(self):
        data = {
            'username': 'egor',
            'password': 'egor',
            're_password': 'egor'
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)\

