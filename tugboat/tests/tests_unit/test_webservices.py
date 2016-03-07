# coding: utf-8
"""
Test webservices
"""

import sys
import os
PROJECT_HOME = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(PROJECT_HOME)

import json
import unittest

from flask import url_for
from flask.ext.testing import TestCase
from tugboat.app import app


class TestBumblebeeView(TestCase):
    """
    A basic base class for all of the tests here
    """

    def create_app(self):
        """
        Create the wsgi application
        """
        app_ = app.create_app()
        return app_

    def test_get_redirect_with_qid(self):
        """
        Tests that when you send a list of bibcodes, you get a queryid URL and
        a redirect status code
        """
        url = url_for('bumblebeeview')
        bibcodes = ['bib1', 'bib2', 'bib3', 'bib4']

        r = self.client.post(url, data=json.dumps(bibcodes))

        self.assertStatus(302, r)
        self.assertEqual(r.text, 'http://newurl.adsabs')


if __name__ == '__main__':
    unittest.main(verbosity=2)
