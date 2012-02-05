# -*- coding: utf-8 -*-

# This software is distributed under the FreeBSD License.
# See the accompanying file LICENSE for details.
#
# Copyright 2012 Benjamin Hepp

import unittest

from pyramid import testing
from pyramid.events import NewRequest

import pyramid_rewrite


class RewriteSubscriberTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include(pyramid_rewrite)

    def tearDown(self):
        testing.tearDown()

    def test_rewrite_rule1(self):
        import wingdbstub
        self.config.add_rewrite_rule(
            r'/abc/qwe(?P<num>[0-9]+)/(?P<op>[a-zA-Z]+)',
            '/%(op)s/%(num)s')
        request = testing.DummyRequest(path='/abc/qwe15/get')
        request.query_string = 'id=123'
        event = NewRequest(request)
        pyramid_rewrite.rewrite_subscriber(event)
        self.assertEqual(request.path_info, r'/get/15')
        self.assertEqual(request.query_string, 'id=123')

    def test_rewrite_rule2(self):
        self.config.add_rewrite_rule(
            r'/(?P<user>[a-zA-Z0-9_]+)/(?P<what>[a-zA-Z0-9_]+)' \
             '/(?P<op>[a-zA-Z]+)',
            '/%(op)s(%(user)s.%(what)s)')
        request = testing.DummyRequest(path='/root/foo/get')
        request.query_string = 'id=123'
        event = NewRequest(request)
        pyramid_rewrite.rewrite_subscriber(event)
        self.assertEqual(request.path_info, r'/get(root.foo)')
        self.assertEqual(request.query_string, 'id=123')

    def test_rewrite_rule3(self):
        self.config.add_rewrite_rule(
            r'/favicon.ico',
            '/static/favicon.ico')
        request = testing.DummyRequest(path='/favicon.ico')
        request.query_string = 'id=123'
        event = NewRequest(request)
        pyramid_rewrite.rewrite_subscriber(event)
        self.assertEqual(request.path_info, r'/static/favicon.ico')
        self.assertEqual(request.query_string, 'id=123')

    def test_rewrite_rule4(self):
        self.config.add_rewrite_rule(
            r'/favicon.ico',
            '/static/favicon.ico')
        request = testing.DummyRequest(path='/favicon.icon')
        request.query_string = 'id=123'
        event = NewRequest(request)
        pyramid_rewrite.rewrite_subscriber(event)
        self.assertEqual(request.path_info, r'/favicon.icon')
        self.assertEqual(request.query_string, 'id=123')


def run():
    unittest.main()

if __name__ == '__main__':
    run()
