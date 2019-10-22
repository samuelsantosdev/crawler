from django.test import TestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from .views.feed_view import FeedViewSet
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
import json, logging


class TokenDBTest(TestCase):
    
    def test_token_generator(self):
        user = User.objects.create(
            password="qwe123",
            last_login=None,
            is_superuser=True,
            username="admin",
            first_name="",
            last_name="",
            email="",
            is_staff=True,
            is_active=True )
        
        self.token = Token.objects.create(user=user)
        self.assertIsNotNone(self.token.key)
        logging.info("test_token_generator OK")

class UserDBTest(TestCase):
    
    def test_create_user(self):
        user = User.objects.create(
            password="qwe123",
            last_login=None,
            is_superuser=True,
            username="admin",
            first_name="",
            last_name="",
            email="",
            is_staff=True,
            is_active=True )
        
        self.assertIsInstance(user, User)
        logging.info("test_create_user OK")

class FeedRestTests(TestCase):

    def test_feed_no_auth(self):
        factory = APIRequestFactory()
        request = factory.get('/feed/')
        view = FeedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 401)
        logging.info("test_feed_no_auth OK")
        

    def test_feed_auth(self):
        factory = APIRequestFactory()

        user = User.objects.create(
            password="qwe123",
            last_login=None,
            is_superuser=True,
            username="admin",
            first_name="",
            last_name="",
            email="",
            is_staff=True,
            is_active=True )
        
        token = Token.objects.create(user=user)

        request = factory.get('/feed/', content_type='application/json')
        force_authenticate(request, user=user, token=token)
        view = FeedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        logging.info("test_feed_auth OK")

    def test_feed_method(self):
        factory = APIRequestFactory()
        user = User.objects.create(
            password="qwe123",
            last_login=None,
            is_superuser=True,
            username="admin",
            first_name="",
            last_name="",
            email="",
            is_staff=True,
            is_active=True )
        
        request = factory.post('/feed/', content_type='application/json')
        force_authenticate(request, user=user)
        view = FeedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 405)
        logging.info("test_feed_method OK")