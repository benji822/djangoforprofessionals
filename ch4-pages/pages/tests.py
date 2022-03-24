from pydoc import resolve
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomepageTest(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.respone = self.client.get(url)

    def test_homepage_statue(self):
        self.assertEqual(self.respone.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.respone, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.respone, 'Homepage')

    def test_homepage_dose_not_contains_incorrect_html(self):
        self.assertNotContains(self.respone, 'This is incorrect')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
