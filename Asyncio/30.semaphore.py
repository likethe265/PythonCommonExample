# coding:utf-8
import time, asyncio, aiohttp


async def hello(i, semaphore):
    async with semaphore:
        print(i)
        await asyncio.sleep(1)


async def run():
    semaphore = asyncio.Semaphore(3)
    to_get = [hello(i, semaphore) for i in range(10)]
    await asyncio.gather(*to_get)


if __name__ == '__main__':
    #    now=lambda :time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
