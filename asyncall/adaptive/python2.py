# -*- coding:utf-8 -*-
# File Name:         python2
# Description:   
# ---
# Author:            tiagn
# Create Datetime:   2018/10/1 21:07
# Update Datetime:   2018/10/1 21:07
# ---


__author__ = 'tiagn'

try:
    import queue
except ImportError:
    import Queue as queue
try:
    import asyncio
except ImportError:
    import trollius as asyncio
from ..util import Result


@asyncio.coroutine
def _work(task, result_queue, no_result, all_result):
    try:
        result = yield asyncio.From(task)
    except Result as e:
        result = e.result
    if no_result:
        return
    if all_result:
        result_queue.put(result)
    else:
        if result:
            result_queue.put(result)
