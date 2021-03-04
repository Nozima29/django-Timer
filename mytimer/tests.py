from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from .forms import TimerForm
from .models import Timer

class MyTimerApp(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
            'start': 24,
            'end': 12
        }

    def test_template(self):
        template = 'index.html'
        response = self.client.get(reverse('create'))
        self.assertTemplateUsed(response, template)

    def test_form_valid(self):
        form = TimerForm(self.data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.data['start'] = None
        form = TimerForm(self.data)
        self.assertFalse(form.is_valid())

    def test_request_POST(self):
        url = reverse('create')
        response = self.client.post(url, self.data)
        self.assertEquals(response.status_code, 200)

        timer = Timer.objects.filter(start=self.data['start'])
        self.assertTrue(timer.exists())

    def test_request_GET(self):
        url = reverse('create')
        response = self.client.get(url, self.data)
        self.assertEquals(response.status_code, 200)

        timer = Timer.objects.filter(start=self.data['start'])
        self.assertFalse(timer.exists())


