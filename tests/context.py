# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from asyncall import task_imap, task_map
from asyncall import imap, map
from asyncall import AsyncTaskManage
from asyncall import AsyncManage
from asyncall import Result
