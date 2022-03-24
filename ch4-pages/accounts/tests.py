from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='ben',
            email='ben@email.com',
            password='ben123'
        )
        self.assertEqual(user.username, 'ben')
        self.assertEqual(user.email, 'ben@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin-user',
            email='admin-user@email.com',
            password='admin123'
        )
        self.assertEqual(admin_user.username, 'admin-user')
        self.assertEqual(admin_user.email, 'admin-user@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
