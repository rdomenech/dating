from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Interest, Member


class MemberTests(APITestCase):
    """
    Member enpoint tests.
    """

    def setUp(self):
        """
        Tests constructor.
        """

        self.interest = Interest.objects.create(name='test_interest')

    def test_create_member_full(self):
        """
        Test members' post endpoint with full data.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.all().count(), 1)
        self.assertEqual(Member.objects.get().user.username, 'myname@test.com')
        self.assertEqual(Member.objects.get().interests.first().name,
                         'test_interest')

    def test_create_member_wrong_interests(self):
        """
        Test members' post endpoint with wrong interests.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'wrong'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.all().count(), 1)
        self.assertEqual(Member.objects.get().user.username, 'myname@test.com')
        self.assertEqual(Member.objects.get().interests.all().count(), 0)

    def test_create_member_no_interests(self):
        """
        Test members' post endpoint with no interests.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': []
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.all().count(), 1)
        self.assertEqual(Member.objects.get().user.username, 'myname@test.com')
        self.assertEqual(Member.objects.get().interests.all().count(), 0)

    def test_create_member_no_age(self):
        """
        Test members' post endpoint with no age.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': None,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_negative_age(self):
        """
        Test members' post endpoint with negative age.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': -10,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_no_gender(self):
        """
        Test members' post endpoint with no gender.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': None,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_negative_gender(self):
        """
        Test members' post endpoint with no gender.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': -1,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_no_password(self):
        """
        Test members' post endpoint with no password.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': 'Name',
            'password': None,
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_no_last_name(self):
        """
        Test members' post endpoint with no last_name.
        """

        url = reverse('members')
        data = {
            'username': 'myname@test.com',
            'first_name': 'My',
            'last_name': '',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_no_username(self):
        """
        Test members' post endpoint with no username.
        """

        url = reverse('members')
        data = {
            'username': '',
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)

    def test_create_member_wrong_body(self):
        """
        Test members' post endpoint with wrong body (not username).
        """

        url = reverse('members')
        data = {
            'first_name': 'My',
            'last_name': 'Name',
            'password': 'test12345',
            'gender': 0,
            'age': 18,
            'interests': [{'id': 1, 'name': 'test_interest'}]
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Member.objects.all().count(), 0)
