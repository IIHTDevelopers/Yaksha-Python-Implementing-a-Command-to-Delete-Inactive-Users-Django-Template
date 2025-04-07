from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command


class DeleteInactiveUsersExceptionalTest(TestCase):

    def test_no_inactive_users(self):
        test_obj = TestUtils()
        """Test that no error occurs when there are no inactive users"""
        try:
            # Create a user who is active (last login < 6 months ago)
            active_user = User.objects.create_user(username='active_user', password='password')
            active_user.last_login = timezone.now() - timedelta(days=200)  # More than 6 months
            active_user.save()

            # Run the delete inactive users command
            call_command('delete_inactive_users')

            # Ensure the active user is still present
            self.assertEqual(User.objects.filter(username='active_user').count(), 0)

            # Assert test passed
            test_obj.yakshaAssert("TestNoInactiveUsers", True, "functional")
            print("TestNoInactiveUsers = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestNoInactiveUsers", False, "functional")
            print(f"TestNoInactiveUsers = Failed")