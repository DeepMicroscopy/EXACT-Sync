# coding: utf-8

"""
    File uploads (create_image and the other endpoints with a file) do not go through
    rest.RESTClientObject but through ApiClient's own requests-based streaming path.

    These tests need no EXACT server: requests.post is replaced by a mock.
"""

from __future__ import absolute_import

import os
import tempfile
import unittest
from unittest import mock

import requests

from exact_sync.v1.api_client import ApiClient
from exact_sync.v1.configuration import Configuration
from exact_sync.v1.api.images_api import ImagesApi
from exact_sync.v1.rest import ApiException

IMAGES = ('{"count": 1, "next": null, "previous": null, "results": [{"id": 5, "name": "a.png", '
          '"filename": "a.png", "image_set": 1, "annotations": []}]}')


def fake_response(status, body, reason='', content_type='application/json'):
    response = requests.Response()
    response.status_code = status
    response.reason = reason
    response._content = body.encode()
    response.headers['Content-Type'] = content_type
    return response


class TestUploadResponses(unittest.TestCase):

    def setUp(self):
        configuration = Configuration()
        configuration.host = 'http://exact.invalid'
        self.api = ImagesApi(ApiClient(configuration), retry=False)
        handle, self.path = tempfile.mkstemp(suffix='.png')
        os.write(handle, b'not really a png')
        os.close(handle)

    def tearDown(self):
        os.remove(self.path)

    def upload(self, *responses):
        with mock.patch('exact_sync.v1.api_client.requests.post', side_effect=list(responses)) as post:
            try:
                return self.api.create_image(file_path=self.path, image_type=0, image_set=1), post
            finally:
                self.post = post

    def uploaded_file(self, call=0):
        encoder = self.post.call_args_list[call][1]['data']
        return encoder.fields['file_path'][1]

    def test_success_is_deserialized(self):
        images, post = self.upload(fake_response(201, IMAGES, 'Created'))
        self.assertEqual(images.results[0].id, 5)
        self.assertEqual(images.results[0].name, 'a.png')
        self.assertTrue(self.uploaded_file().closed)

    def test_with_http_info_returns_status_and_headers(self):
        with mock.patch('exact_sync.v1.api_client.requests.post', return_value=fake_response(201, IMAGES, 'Created')):
            images, status, headers = self.api.create_image_with_http_info(
                file_path=self.path, image_type=0, image_set=1)
        self.assertEqual(images.results[0].id, 5)
        self.assertEqual(status, 201)
        self.assertEqual(headers['Content-Type'], 'application/json')

    def test_error_status_raises_api_exception(self):
        body = '{"detail": "You do not have permission to perform this action."}'
        with self.assertRaises(ApiException) as context:
            self.upload(fake_response(403, body, 'Forbidden'))
        self.assertEqual(context.exception.status, 403)
        self.assertEqual(context.exception.reason, 'Forbidden')
        self.assertEqual(context.exception.body, body.encode())
        self.assertIn('permission', str(context.exception))
        self.assertTrue(self.uploaded_file().closed)

    def test_error_page_that_is_not_json_raises_api_exception(self):
        with self.assertRaises(ApiException) as context:
            self.upload(fake_response(502, '<html>Bad Gateway</html>', 'Bad Gateway', 'text/html'))
        self.assertEqual(context.exception.status, 502)

    def test_gateway_error_is_retried(self):
        self.api.retry = True
        self.api.retry_backoff = 0
        images, post = self.upload(fake_response(503, '', 'Service Unavailable', 'text/html'),
                                   fake_response(201, IMAGES, 'Created'))
        self.assertEqual(images.results[0].id, 5)
        self.assertEqual(post.call_count, 2)
        self.assertTrue(self.uploaded_file(0).closed and self.uploaded_file(1).closed)


if __name__ == '__main__':
    unittest.main()
