from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestUFView(TestCase):
    url = reverse('uf-list')

    def test_endpoint_200_database_without_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_endpoint_200_database_with_data(self):
        url = self.url + '01-01-2022/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 365)

    def test_endpoint_404(self):
        wrong_url = self.url + '//1'
        response = self.client.get(wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestUFDetailAPIView(TestCase):
    url = reverse('uf-list')

    def test_endpoint_200(self):
        url = self.url + '01-01-2023/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_date(self):
        url = self.url + '21-04-2023/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data[0]['value']), float)

    def test_invalid_date_before_2013(self):
        url = self.url + '21-04-2012/'
        response = self.client.get(url)
        error_string = '["Year must be greater than or equal to 2013"]'
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), error_string)

    def test_invalid_date_after_2023(self):
        url = self.url + '21-04-2024/'
        response = self.client.get(url)
        error_string = ('["The UF value is not available for the specified '
                        'date. Please check again on the 9th day of the '
                        'month when the value could be set."]')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), error_string)
