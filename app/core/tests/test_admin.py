from django.test import TestCase, Client
from django.contrib.auth import get_user_model

# Generate urls from djando admin page
from django.urls import reverse

class AdminSiteTests(TestCase):
  # setup function to run before every test runs
  def setUp(self):
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser(
      email='admin@gmail.com',
      password='test123'
    )
    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
      email='test@gmail.com',
      password='test123',
      name='Test user full name'
    )

  def test_users_listed(self):
    """Test that users are listed on users page"""
    url = reverse('admin:core_user_changelist')
    res = self.client.get(url)

    self.assertContains(res, self.user.name)
    self.assertContains(res, self.user.email)

  def test_user_change_page(self):
    """Test that user edit page works"""
    # /admin/core/user/{args}
    url = reverse('admin:core_user_change', args=[self.user.id])

    # http GET on url
    res = self.client.get(url)

    self.assertEqual(res.status_code, 200)