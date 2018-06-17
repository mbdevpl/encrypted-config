
import logging
import unittest

from encrypted_config.json_transform import json_coordinate

_LOG = logging.getLogger(__name__)


class Tests(unittest.TestCase):

    def test_resolve_coordinate(self):
        example = {
            'test': {
                'account1': [['a', 'b'], [{'good': True, 'bad': False}, 'd']],
                'account2': {'login': 'test', 'password': 'blah'},
                'account3': {'quote': ['to', 'be', 'or', 'not', 'to be']}},
            'production': False}
        for coordinate in {
                'test.account2.password', 'production', 'test.account3.quote.1',
                'test.account3.quote', 'test.account1.1.0.good'}:
            getter, setter = json_coordinate(example, coordinate)
            original_value = getter()
            _LOG.debug('data at %s is %s', coordinate, getter())
            setter('new_value')
            self.assertEqual(getter(), 'new_value')
            getter2, setter2 = json_coordinate(example, coordinate)
            self.assertEqual(getter(), 'new_value')
            self.assertEqual(getter2(), 'new_value')
            setter2(original_value)
            self.assertEqual(getter(), original_value)
            getter, _ = json_coordinate(example, coordinate)
            self.assertEqual(getter(), original_value)
