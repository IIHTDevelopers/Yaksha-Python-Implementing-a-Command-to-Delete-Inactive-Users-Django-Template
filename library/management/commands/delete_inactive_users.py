
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

class Command(BaseCommand):
    help = 'Deletes all inactive users who have not logged in within the past 6 months.'

    def handle(self, *args, **kwargs):
        pass

