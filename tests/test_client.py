import requests_mock
import unittest
import os

from seguia.client import Client

class TestClient(unittest.TestCase):

	def setUp(self):
		self.client = Client(hostname='https://example.com')

	@requests_mock.Mocker()
	def test_search_returns_an_empty_json_array(self, mock):
		mock.get('/data?', json=[], status_code=200)
		json = self.client.search()
		assert json == []


	@requests_mock.Mocker()
	def test_search_returns_a_list_of_found_data(self, mock):
		data1 = { 'id': '5e63f5c3-9d50-41d2-8de5-a2f5d36c98e5', 'format': 'csv'}
		data2 = { 'id': '5c221b64-adec-469e-be06-50cf7c1047b5', 'format': 'txt'}
		data3 = { 'id': 'e4a9863f-4d1c-48f1-9552-9b27dda41998', 'format': 'csv'}
		mock.get('/data', json=[], status_code=200)
		mock.get('/data?format=csv', json=[data1, data3], status_code=200)
		json = self.client.search(format='csv')
		assert json == [data1, data3]

