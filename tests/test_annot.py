#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_annots
----------------------------------

Tests for `annots` module.
"""


import sys
import unittest

from annot import annots
from annot._utils import _annotations_to_script, _annotations_to_init


class TestUtils(unittest.TestCase):
    # TODO: add more tests
    def setUp(self):
        self.init_pattern = """\
def __init__(self, username: str, password: str):
    self.username = username
    self.password = password
"""
        self.annotations = {'username': str, 'password': str}

    def test__annotations_to_script(self):
        init_string = _annotations_to_script(self.annotations, post_init=False)

        self.assertEquals(self.init_pattern, init_string)

    def test__annotation_to_script_with_additional_call(self):
        self.init_pattern += '    self.__annots_post_init__()\n'
        init_string = _annotations_to_script(self.annotations, post_init=True)

        self.assertEquals(self.init_pattern, init_string)
