#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ted Liang'

'''
JSON API definition.
'''

import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which constains error(required),
    data(optional) and message(optional).
    '''

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    value error or invalid.
    '''

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    resource was not found.
    '''


    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('valud:notfound', field, message)

class APIPermissionError(APIError):
    '''
    no permission
    '''

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)