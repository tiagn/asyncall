# -*- coding:utf-8 -*-
# File Name:         python3
# Description:   
# ---
# Author:            tiagn
# Create Datetime:   2018/10/1 21:07
# Update Datetime:   2018/10/1 21:07
# ---

__author__ = 'tiagn'
from tests.context import Result
import asyncio

@asyncio.coroutine
def demo(name):
    import random
    asleep = random.randint(0, 1)
    print('---start, %s  %s' % (name, asleep))
    yield from asyncio.sleep(asleep)
    print('---stop, %s' % name)
    raise Result(name)