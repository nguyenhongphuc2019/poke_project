from django.contrib.auth import models
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Pokemon

TEST_USER = {
    'username': 'phuc',
    'email': 'test@test.com',
    'password': make_password('123456')
}

MESSAGES_FAILURE = {
    'no_active_account': 'No active account found with the given credentials',
    'token_not_valid_or_expires': 'Given token not valid for any token type',
    'unauthorized': 'Authentication credentials were not provided.'
}


class TestLogin(APITestCase):

    def setUp(self) -> None:
        models.User.objects.create(**TEST_USER)

    def test_login_successfully(self):

        response = APIClient().post('/login', data={'username': 'phuc', 'password': '123456'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['access'])
        self.assertIsNotNone(response.data['refresh'])

    def test_login_failure(self):
        client = APIClient()
        response = client.post('/login', data={'username': 'phuc', 'password': '1'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], MESSAGES_FAILURE['no_active_account'])


class TestAPI(APITestCase):

    def setUp(self) -> None:
        models.User.objects.create(**TEST_USER, is_active=True, is_staff=True, is_authenticated=True)
        for i in range(5):
            Pokemon.objects.create(name=f'Pokemon_{i}')

    # def test_get_list_pokemon_successfully(self):
    #     user_login = APIClient().post('/login', data={'username': 'phuc', 'password': '123456'})
    #     access_token = user_login.data['access']
    #     response = APIClient().get('/api/v1/pokemon/', headers={
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {access_token}'
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['count'], 5)

    # def test_get_list_pokemon_without_jwt_token(self):
    #     access_token = None
    #     response = APIClient().get('/api/v1/', headers={
    #         'Authorization': f'Bearer {access_token}',
    #         'Content-Type': 'application/json'
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(response.data['detail'], MESSAGES_FAILURE['unauthorized'])
