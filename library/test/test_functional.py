from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Event
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command

class DeleteInactiveUsersFunctionalTest(TestCase):

    def test_delete_inactive_users(self):
        test_obj = TestUtils()

        """Test that inactive users are deleted successfully"""
        try:
            # Create a user who is inactive (last login > 6 months ago)
            inactive_user = User.objects.create_user(username='inactive_user', password='password')
            inactive_user.last_login = timezone.now() - timedelta(days=200)  # More than 6 months
            inactive_user.save()

            # Run the delete inactive users command
            call_command('delete_inactive_users')

            # Ensure the user is deleted
            self.assertEqual(User.objects.filter(username='inactive_user').count(), 0)

            # Assert test passed
            test_obj.yakshaAssert("TestDeleteInactiveUsers", True, "functional")
            print("TestDeleteInactiveUsers = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestDeleteInactiveUsers", False, "functional")
            print(f"TestDeleteInactiveUsers = Failed")