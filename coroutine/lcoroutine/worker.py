# coding: utf-8
import asyncio
from concurrent.futures import ThreadPoolExecutor

from .manager import TaskCenter


class Concurrent(object):
    def __init__(self, workers: int):
        self.center = TaskCenter()
        self.executor = ThreadPoolExecutor(workers)
        self.loop = asyncio.get_event_loop()

    async def _add_task(self, func, *args):
        return await self.loop.run_in_executor(self.executor, func, *args)

    # 同步添加异步任务
    def add_task(self, func, *args):
        self.center.tasks.append(self._add_task(func, *args))

    # 并行执行异步任务并阻塞直到全部
    def wait(self):
        self.center.results = self.loop.run_until_complete(asyncio.gather(*self.center.tasks))
        # 清空上次任务
        self.center.tasks = []
        return self.center.results

    def close(self):
        self.executor.shutdown()
        self.loop.close()
