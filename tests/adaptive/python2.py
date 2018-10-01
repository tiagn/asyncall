# -*- coding:utf-8 -*-
# File Name:         python2
# Description:   
# ---
# Author:            tiagn
# Create Datetime:   2018/10/1 21:07
# Update Datetime:   2018/10/1 21:07
# ---

__author__ = 'tiagn'

from ..context import Result
import random

try:
    import asyncio
except ImportError:
    import trollius as asyncio

@asyncio.coroutine
def demo(name):
    asleep = random.randint(0, 1)
    print('---start, %s  %s' % (name, asleep))
    yield asyncio.sleep(asleep)
    print('---stop, %s' % name)
    raise Result(name)
