#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ted Liang'

from coroweb import get, post
from models import User, next_id, Blog, Comment
import re, time, json, logging, hashlib, base64, asyncio

@get('/')
def index(request):
    # users = yield from User.findAll()
    # return {
    #     '__template__': 'test.html',
    #     'users':users
    # }

    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test  Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__':'blogs.html',
        'blogs':blogs
    }


@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = 'centerm'
    return dict(users=users)