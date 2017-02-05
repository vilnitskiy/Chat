import mock

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from chat.models import Room


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        """ test for home view """
        self.url = reverse('home')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Sign in with Facebook', response.content)

    def test_new_room(self):
        """ test for new_room view """
        self.url = reverse('new_room')
        response = self.client.get(self.url)
        test_label = Room.objects.last().label
        expected_url = reverse('room', kwargs={'label': test_label})
        self.assertRedirects(response, expected_url)

    def test_room(self):
        """ test for room view """
        Room.objects.create(label='test_label')
        self.url = reverse(
            'room',
            kwargs={'label': 'test_label'}
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test_label', response.content)
