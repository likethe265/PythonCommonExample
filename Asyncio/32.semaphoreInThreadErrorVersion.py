# coding:utf-8
import time, asyncio, aiohttp
from threading import Thread


async def hello(i, semaphore):
    async with semaphore:
        print(i)
        await asyncio.sleep(1)


async def run(semaphore):
    for i in range(10):
        asyncio.run_coroutine_threadsafe(hello(i, semaphore), new_loop)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == '__main__':
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    semaphore = asyncio.Semaphore(
        3)  # create semaphore outside the async thread will only run the first 3 entries(I set semaphore size to 3)
    asyncio.run_coroutine_threadsafe(run(semaphore), new_loop)
    t.join()
