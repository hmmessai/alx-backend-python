#!/usr/bin/env python3
"""Test for the utils.acess_nested_map function
"""
from utils import (access_nested_map, get_json)
from parameterized import parameterized, parameterized_class
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_acess_nested_map(
            self,
            nes_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests the return value of anm"""
        self.assertEqual(access_nested_map(nes_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nes_map, path, expected):
        with self.assertRaises(KeyError) as e:
            result = access_nested_map(nes_map, path)
            self.assertEqual(e, expected)


class TestGetJson(unittest.TestCase):
    """Tests get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests if the get_json method
        returns the expected result"""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Tests m"""
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
