#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
import ted_orm
import logging
import sys
from models import User, Blog, Comment


l = logging.getLogger(__name__)
l.setLevel(logging.DEBUG)


def test(loop):
    yield from ted_orm.create_pool(loop,
        user='root',
        password='centerm',
        db='awesome'
    )

    # u = User(name='lx2', email='lx2@example.com', passwd='1234567890', image='about:lx2')
    #
    # yield from u.save()


    users = yield from User.findAll(orderBy='created_at')
    # for u in users:
    #     l.info('name: %s, email: %s' % (u.name, u.email))

    # user = users[1]
    # l.info('name:%s, email: %s' % (user.name, user.email))
    # user.name = 'liangxu_U'
    # user.email = 'U_lx@emali.com'
    # yield from user.update()

    users_del = yield from User.findAll(orderBy='created_at', limit=(1, 2))
    for ud in users_del:
        l.info('del user : %s ' % ud.name)
        yield from ud.remove()




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)


