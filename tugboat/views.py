# encoding: utf-8
"""
Views
"""
import requests
from requests.exceptions import ConnectionError
from flask import current_app, render_template, make_response
from flask.ext.restful import Resource
from cache import cache

MINUTES = 60.0  # seconds
SYSTEMSGO_CACHE_TIMEOUT = 5*MINUTES

class BumblebeeView(Resource):
    """
    End point that is used to forward a search result page from ADS Classic
    to ADS Bumblebee
    """
    def post(self):
        """
        HTTP GET request

        There are two simple steps:
            1. Send a query to myads-service in 'store-query' that contains
               the list of bibcodes in the user's ADS Classic search
            2. Return a URL with the relevant queryid that the user can be
               forwarded to

        When the user clicks the URL, it will use execute-query to run the
        relevant query via Solr's Bigquery.

        Returns:
        302: redirect to the relevant URL

        :return: str
        """

        # return redirect('', code=302)
        return 200, 'blah'