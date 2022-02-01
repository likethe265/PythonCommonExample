import asyncio
import datetime
import time
from random import randrange
from threading import Thread


async def task0(idx):
    await asyncio.sleep(1.5)
    print(f'task0, idx:{idx}')


async def task1(idx):
    await asyncio.sleep(1.8)
    print(f'task1, idx:{idx}')


async def pairTask(idx):
    tasks = []
    tasks.append(task0(idx))
    tasks.append(task1(idx))
    await asyncio.gather(*tasks)
    print(f'tasks done: {idx}.')


async def launcher(idx):
    while True:
        tasks = []
        tasks.append(pairTask(idx))
        tasks.append(asyncio.sleep(4))
        await asyncio.gather(*tasks)
        print(f'circle: {idx} done.')


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

asyncio.run_coroutine_threadsafe(launcher(1), new_loop)
time.sleep(1)
asyncio.run_coroutine_threadsafe(launcher(2), new_loop)
time.sleep(1)
asyncio.run_coroutine_threadsafe(launcher(3), new_loop)
