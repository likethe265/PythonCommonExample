# coding:utf-8
import time, asyncio, aiohttp
from threading import Thread

semaphore = None


async def hello(i, semaphore):
    async with semaphore:
        print(i)
        await asyncio.sleep(1)


async def createSemaphore():
    global semaphore
    semaphore = asyncio.Semaphore(3)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == '__main__':
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    future = asyncio.run_coroutine_threadsafe(createSemaphore(), new_loop)
    for i in range(10):
        asyncio.run_coroutine_threadsafe(hello(i, semaphore), new_loop)
    t.join()
