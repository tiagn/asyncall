# -*- coding:utf-8 -*-
# File Name:         python3
# Description:   
# ---
# Author:            tiagn
# Create Datetime:   2018/10/1 21:07
# Update Datetime:   2018/10/1 21:07
# ---
from ..util import Result

__author__ = 'tiagn'
import asyncio

@asyncio.coroutine
def _work(task, result_queue, no_result, all_result):
    try:
        result = yield from task
    except Result as e:
        result = e.result
    if no_result:
        return
    if all_result:
        result_queue.put(result)
    else:
        if result:
            result_queue.put(result)
