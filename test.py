import unittest

from pyresult import ok, error
from pyresult.pyresult import Result


class TestPyResult(unittest.TestCase):
    def test_ok(self):
        self.assertIsInstance(ok(), Result)

    def test_ok_value(self):
        self.assertEqual(ok('test ok').value, 'test ok')

    def test_ok_is_error(self):
        self.assertTrue(ok('test ok').is_ok())

    def test_ok_repr(self):
        self.assertEqual(str(ok('test ok')), 'Result: status: True; value: test ok')

    def test_error(self):
        self.assertIsInstance(error(), Result)

    def test_error_value(self):
        self.assertEqual(error('test error').value, 'test error')

    def test_error_is_error(self):
        self.assertFalse(error('test error').is_ok())

    def test_error_repr(self):
        self.assertEqual(str(error('test error')), 'Result: status: False; value: test error')
