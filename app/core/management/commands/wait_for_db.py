"""
Djago command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as PsyCoopg2Error
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for databse"""

    def handle(self, *args, **options):
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try: 
                self.check(databases=['default'])
