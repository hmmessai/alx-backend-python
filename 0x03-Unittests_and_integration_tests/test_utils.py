#!/usr/bin/env python3
"""Test for the utils.acess_nested_map function
"""
from utils import access_nested_map as anm
from parameterized import parameterized, parameterized_class
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
    def test_acess_nested_map(self, nes_map, path, expected):
        """Tests the return value of anm"""
        self.assertEqual(anm(nes_map, path), expected)

    @parameterized.expand([
                    ({}, ("a",), "a"),
                    ({"a": 1}, ("a", "b"), "b")
                    ])
    def test_access_nested_map_exception(self, nes_map, path, expected):
        with self.assertRaises(KeyError) as e:
            result = anm(nes_map, path)
            self.assertEqual(e, expected)


class TestGetJson(unittest.TestCase):
    """Tests get_json method
    """
    @parameterized.expand([
                    ("http://example.com", {"payload": True}),
                    ("http://holberton.io", {"payload": False})
                    ])
    def test_get_json(self):
        """Tests if the get_json method
        returns the expected result"""
        result = anm(nes_map, path)1
        result = anm(nes_map, path)1


if __name__ == '__main__':
    unittest.main()
