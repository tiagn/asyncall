# /usr/bin/env python
# -*- coding:utf-8 -*-

import pytest

from tests.context import *

import logging

logging.basicConfig()

try:
    import asyncio
except ImportError:
    import trollius as asyncio

import sys

if '2' == sys.version[0]:
    from tests.adaptive.python2 import demo
    from tests.adaptive.python2 import demo2
else:
    from tests.adaptive.python3 import demo
    from tests.adaptive.python3 import demo2

__author__ = 'tiagn'


def test_AsyncManage():
    am = AsyncManage()
    tasks = [demo('A'), demo('B'), demo('C')]
    tasks2 = [demo('A'), demo('B'), demo('C')]
    result = ['A', 'B', 'C']

    res = am.imap(tasks)
    for r in res:
        assert r in result
    for r in am.map(tasks2):
        assert r in result


def test_AsyncTaskManage():
    tasks = ['A', 'B', 'C']
    atm = AsyncTaskManage(demo)
    res = atm.imap(tasks)
    for r in res:
        assert r in tasks
    for r in atm.map(tasks):
        assert r in tasks


def test_map():
    tasks = [demo('A'), demo('B'), demo('C')]
    tasks2 = [demo('A'), demo('B'), demo('C')]
    result = ['A', 'B', 'C']
    res = imap(tasks)
    for r in res:
        assert r in result
    res = map(tasks2)
    for r in res:
        assert r in result


def test_task_map():
    tasks = ['A', 'B', 'C']

    res = task_imap(tasks, async_func=demo)
    for r in res:
        assert r in tasks
    res = task_map(tasks, async_func=demo)
    for r in res:
        assert r in tasks


def test_neste_loop():
    paras = [test_task_map, test_map]
    res = task_map(paras, async_func=demo2)
    for r in res:
        assert r in paras
    res = task_imap(paras, async_func=demo2)
    for r in res:
        assert r in paras


if __name__ == '__main__':
    pytest.main()
