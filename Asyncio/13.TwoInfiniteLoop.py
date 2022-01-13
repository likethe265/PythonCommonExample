import asyncio
import contextlib
import time


async def loop0():
    while 1:
        print('Loop0 running...')
        await asyncio.sleep(1)


async def loop1():
    while 1:
        print('Loop1 running...')
        await asyncio.sleep(1)


async def schedule2Loops():
    tasks = [
        asyncio.ensure_future(loop0()),
        asyncio.ensure_future(loop1())]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(schedule2Loops())
