# patch() allows us to mock the behaviour of the django getDB()
from unittest.mock import patch

# allows us call command in our source code
from django.core.management import call_command

# operational error django throws when db is unavailable
from django.db.utils import OperationalError

# test case
from django.test import TestCase

class CommandTests(TestCase):
  def test_wait_for_db_ready(self):
    """Test waiting for db when db is available"""
    # mock behaviour of getItem() using patch() hich is assign as a variable gi
    with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
      gi.return_value = True
      call_command('wait_for_db')
      self.assertEqual(gi.call_count, 1)

  @patch('time.sleep', return_value=True)
  def test_wait_for_db(self, ts):
    """Test waiting fro db"""
    with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
      gi.side_efffect = [OperationalError] * 5 + [True]
      call_command('wait_for_db')
      self.assetEqual(gi.call_count, 6)