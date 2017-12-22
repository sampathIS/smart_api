#!/usr/bin/env python

import requests
from jsonmerge import merge as combine


class APIRequest(object):
    """
    Module for CSP API Validations
    """
    def __init__(self, measurement):
        """
        Initialization for Request Validation

        :param measurement: Provide Influx DB measurement name
        """
        self.app_token = None
        self.measurement = measurement

    def merge(self, headers):
        """
        Perform merge of headers with Authorization JSON

        :param headers: Provide headers in JSON
        :return: Returns merged headers
        :rtype: dict
        """
        authorization = {"Authorization": "Bearer %s" % self.app_token.access_token}
        merge = combine(headers, authorization)
        return merge

    def get(self, url, headers, proxies=None):
        """
        Perform GET request method

        :param url: Provide get request URL
        :param headers: Provide headers in JSON
        :param proxies: Provides proxy server in JSON format
        :return: Returns get request response in dictionary
        :rtype: dict
        """
        method = requests.get(url=url, headers=self.merge(headers=headers), proxies=proxies)
        return method

    def post(self, url, headers, proxies=None, data=None):
        """
        Perform POST request method

        :param url: Provide post request URL
        :param headers: Provide headers in JSON
        :param proxies: Provides proxy server in JSON format
        :param data: Provide payload data
        :return: returns response in dictionary
        :rtype: dict
        """
        method = requests.post(url=url, headers=self.merge(headers=headers), data=data, proxies=proxies)
        return method