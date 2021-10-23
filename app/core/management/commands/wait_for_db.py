"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 23/10/21
@name: wait_for_db
"""

import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to pause execution until database is available """

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except  OperationalError:
                self.stdout.write("Database unavailable...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available...'))
