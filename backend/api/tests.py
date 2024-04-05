import base64
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from common.constants import StatusChoices

PASSWORD = 'admin123!'


def create_user(user_status, username, password=PASSWORD):
    return get_user_model().objects.create_user(
        username=username,
        first_name='Test',
        last_name='User',
        password=password,
        status=user_status
    )


class AuthenticationTest(APITestCase):
    def setUp(self):
        self.user_active_status = create_user(
            username="test@gmail.ru",
            user_status=StatusChoices.ACTIVE
        )
        self.user_nonactive_status = create_user(
            username="test1@gmail.ru",
            user_status=StatusChoices.BLOCKED
        )

    def test_user_can_sign_up(self):
        response = self.client.post(
            reverse('sign_up'),
            data={
                'username': 'user@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'password': PASSWORD,
                'password_confirm': PASSWORD,
                'status': StatusChoices.ACTIVE
            })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)

    def test_user_can_log_in(self):
        response = self.client.post(
            reverse('log_in'),
            data={
                'username': self.user_active_status.username,
                'password': PASSWORD,
            }
        )

        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(payload_data['user_id'], self.user_active_status.id)
        self.assertEqual(payload_data['username'], self.user_active_status.username)
        self.assertEqual(payload_data['first_name'], self.user_active_status.first_name)


class ClientTest(APITestCase):

    def setUp(self):
        self.user_active_status = create_user(
            username="test@gmail.ru",
            user_status=StatusChoices.ACTIVE
        )
        self.user_nonactive_status = create_user(
            username="test1@gmail.ru",
            user_status=StatusChoices.BLOCKED
        )
        self.user_data = self.user_nonactive_status
        response = self.client.post(
            reverse('log_in'),
            data={
                'username': self.user_active_status.username,
                'password': PASSWORD,
            }
        )
        self.access_token = response.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_active_client_list(self):
        response = self.client.get('/api/v1/clients/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 1)
        response = response.json()
        self.assertEqual(response[0].get('username'), self.user_active_status.username)
