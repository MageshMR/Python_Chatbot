
# Create your tests here.
from django.test import TestCase, Client
import json

class ChatbotAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chat_hello(self):
        response = self.client.post('/chat/', data=json.dumps({'message': 'hello'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('reply', response.json())
        self.assertIn('hello', response.json()['reply'].lower())

    def test_chat_bye(self):
        response = self.client.post('/chat/', data=json.dumps({'message': 'bye'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('goodbye', response.json()['reply'].lower())

    def test_chat_unknown(self):
        response = self.client.post('/chat/', data=json.dumps({'message': 'what is the meaning of life?'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('not sure', response.json()['reply'].lower())

    def test_chat_no_message(self):
        response = self.client.post('/chat/', data=json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('please provide a message', response.json()['reply'].lower())
