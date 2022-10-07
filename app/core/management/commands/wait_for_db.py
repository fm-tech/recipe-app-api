"""
Djago command to wait for the database to be available.
"""
from sqlite3 import OperationalError
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
                self.check(databases=["default"])
                db_up = True
            except (PsyCoopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available"))
