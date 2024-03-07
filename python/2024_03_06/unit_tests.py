import hug
import unittest
import httpserver


class TestAll(unittest.TestCase):

    def test_http_server(self):
        r1 = hug.test.get(httpserver, 'add_numbers', {'a': '1,2,3'})
        self.assertEqual(r1.status, '200 OK')
        self.assertEqual(r1.data, 'New list is [1, 2, 3]')
        r = hug.test.get(httpserver, 'find_number', {'num': 1})
        self.assertEqual(r.status, '200 OK')
        self.assertEqual(r.data, '1 found in list at index 0')

    def test_find_number(self):
        r = hug.test.get(httpserver, 'find_number', {'num': 1})
        self.assertEqual(r.status, '200 OK')
        self.assertEqual(r.data, '1 not found in list []')


if __name__ == '__main__':
    unittest.main()