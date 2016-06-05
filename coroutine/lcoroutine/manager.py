# coding: utf-8
from typing import Awaitable


class TaskCenter(object):
    def __init__(self):
        self.tasks: [Awaitable] = []
        self.results = []
