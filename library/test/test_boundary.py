from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from library.models import Event
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.management import call_command


class DeleteInactiveUsersBoundaryTest(TestCase):

    def test_user_created_exactly_6_months_ago(self):
        test_obj = TestUtils()
        """Test that a user created exactly 6 months ago is considered inactive"""
        try:
            # Create a user who is exactly 6 months old (last login > 6 months ago)
            boundary_user = User.objects.create_user(username='boundary_user', password='password')
            boundary_user.last_login = timezone.now() - timedelta(days=180)  # Exactly 6 months ago
            boundary_user.save()

            # Run the delete inactive users command
            call_command('delete_inactive_users')

            # Ensure the boundary user is deleted
            self.assertEqual(User.objects.filter(username='boundary_user').count(), 0)

            # Assert test passed
            test_obj.yakshaAssert("TestUserCreatedExactly6MonthsAgo", True, "boundary")
            print("TestUserCreatedExactly6MonthsAgo = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestUserCreatedExactly6MonthsAgo", False, "boundary")
            print(f"TestUserCreatedExactly6MonthsAgo = Failed")