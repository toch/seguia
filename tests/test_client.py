import requests_mock
import unittest
import os
import tempfile
import filecmp

from seguia.client import Client

class TestClient(unittest.TestCase):

	def setUp(self):
		self.client = Client(hostname='https://example.com')

	@requests_mock.Mocker()
	def test_search_returns_an_empty_json_array(self, mock):
		mock.get('/data', json=[], status_code=200)
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

	@requests_mock.Mocker()
	def test_index_curates_data_and_returns_an_id(self, mock):
		data = { 'format': 'csv' }
		created_data = { 'id': 'd8c77454-093d-4a44-a53b-2970f9f942b1', 'format': 'csv'}
		mock.post('/data', json=created_data, status_code=202)
		json = self.client.index(data)
		assert json['id'] is not None

	@requests_mock.Mocker()
	def test_upload_pushes_the_data_into_oasis(self, mock):
		id = '9e2398f8-be14-4365-b09e-31bcec9d7a47'
		file = 'tests/fixtures/example.csv'
		mock.put('/data/' + id, status_code=307, headers={'Location': 'https://s3.amazon.com/oasis/1'})
		mock.put('https://s3.amazon.com/oasis/1', status_code=200)
		assert self.client.upload(id, os.path.abspath(file)) == True

	@requests_mock.Mocker()
	def test_download_pulls_the_data_from_oasis(self, mock):
		id = '9e2398f8-be14-4365-b09e-31bcec9d7a47'
		expected_file = 'tests/fixtures/example.csv'
		mock.get('/data/' + id, status_code=307, headers={'Location': 'https://s3.amazon.com/oasis/1'})
		with open(expected_file, 'rb') as data:
			mock.get('https://s3.amazon.com/oasis/1', content=data.read(), status_code=200)

		with tempfile.NamedTemporaryFile() as file:
			self.client.download(id, file.name)
			assert filecmp.cmp(file.name, os.path.abspath(expected_file))




