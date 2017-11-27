import datetime
import json
import unittest
import six

import jsondate


class RoundTripCases(object):

    def _test_roundtrip(self, input, expected=None, test_types=False):
        output = self.roundtrip(input)
        expected = expected if expected else input
        self.assertEqual(output, expected)
        return output

    def test_empty(self):
        self._test_roundtrip({})

    def test_none(self):
        self._test_roundtrip(dict(foo=None))

    def test_datetime(self):
        orig_dict = dict(created_at=datetime.datetime(2011, 1, 1))
        self._test_roundtrip(orig_dict)

    def test_date(self):
        orig_dict = dict(created_at=datetime.date(2011, 1, 1))
        self._test_roundtrip(orig_dict)

    def test_datelike_string(self):
        "A string that looks like a date *will* be interpreted as a date."
        orig_dict = dict(created_at='2011-01-01')
        expected = dict(created_at=datetime.date(2011, 1, 1))
        self._test_roundtrip(orig_dict, expected)

    @staticmethod
    def _strdict(T):
        return { T('foo'): T('bar'), T('empty'): T('') }

    def _test_string_roundtrips(self, intype, outtype):
        input = self._strdict(intype)
        expected = self._strdict(six.text_type)
        output = self._test_roundtrip(input, expected)
        for k, v in six.iteritems(output):
            self.assertEqual(type(k), outtype)
            self.assertEqual(type(v), outtype)

    def test_str_roundtrips(self):
        self._test_string_roundtrips(str, six.text_type)

    def test_unicode_roundtrips(self):
        self._test_string_roundtrips(six.text_type, six.text_type) 


class DumpsLoadsTests(RoundTripCases, unittest.TestCase):

    @staticmethod
    def roundtrip(input):
        return jsondate.loads(jsondate.dumps(input))


class DumpLoadTests(RoundTripCases, unittest.TestCase):

    @staticmethod
    def roundtrip(input):
        fileobj = six.StringIO()
        jsondate.dump(input, fileobj)
        fileobj.seek(0)
        return jsondate.load(fileobj)


class UnexpectedTypeTests(unittest.TestCase):

    def test_unexpected_type_raises(self):
        dict_ = {'foo': set(['a'])}
        with self.assertRaises(TypeError):
            jsondate.dumps(dict_)
