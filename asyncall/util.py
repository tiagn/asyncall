# -*- coding:utf-8 -*-
# File Name:         util
# Description:   
# ---
# Author:            tiagn
# Create Datetime:   2018/10/1 21:09
# Update Datetime:   2018/10/1 21:09
# ---

__author__ = 'tiagn'


class Result(Exception):

    def __init__(self, data):
        self.result = data
