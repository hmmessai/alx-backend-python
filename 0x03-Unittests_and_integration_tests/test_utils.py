#!/usr/bin/env python3
"""Test for the utils.acess_nested_map function
"""
from utils import access_nested_map as anm
from parameterized import parameterized, parameterized_class
import unittest


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


if __name__ == '__main__':
    unittest.main()
