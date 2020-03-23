# time() is used for making the application sleep for some seconds in between each db chek
import time

# connection() tests if db connection is available 
from django.db import connections
from django.db.utils import OperationalError
from django.core.managemnt.base import BaseCommand

class Command(BaseCommand):
  """Djanfo command to pause execution until db is available"""
  # args and options allow us parse custom arguments and options to management commands
  def handle(self, *args, **options):
    self.stdout.write('Waiting for database')
    db_conn = None
    while not db_conn:
      try:
        db_conn = connections['default']
      except OperationalError:
        self.stdout.write('Database unavailable, waiting 1 second')
        time.sleep(1)

    self.stdout.write(self.style.SUCCESS('Databse availabe!'))