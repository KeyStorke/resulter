import unittest

from resulter import ok, error, resultify, Result


class TestResulter(unittest.TestCase):
    def test_ok(self):
        self.assertIsInstance(ok(), Result)

    def test_ok_value(self):
        self.assertEqual(ok('test ok').value, 'test ok')

    def test_ok_is_error(self):
        self.assertTrue(ok('test ok').is_ok())

    def test_ok_repr(self):
        self.assertEqual(str(ok('test ok')), 'Result: status: True; value: test ok')

    def test_resultify_ok(self):
        func = resultify(lambda x: x+1)
        result = func(10)
        self.assertIsInstance(result, Result)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.value, 11)

    def test_error(self):
        self.assertIsInstance(error(), Result)

    def test_error_value(self):
        self.assertEqual(error('test error').value, 'test error')

    def test_error_is_error(self):
        self.assertFalse(error('test error').is_ok())

    def test_error_repr(self):
        self.assertEqual(str(error('test error')), 'Result: status: False; value: test error')

    def test_resultify_error(self):
        func = resultify(lambda x: x/0)
        result = func(10)
        self.assertIsInstance(result, Result)
        self.assertFalse(result.is_ok())
        self.assertIsInstance(result.value, ZeroDivisionError)
