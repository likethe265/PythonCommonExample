import asyncio
import contextlib
import time

now = lambda: time.time()


async def do_something_else():
    i = 0
    while i <= 5:
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do something else {}'.format(currentTime, i))
        await asyncio.sleep(1)
        i += 1


async def do_some_work():
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('do some work start')
    await asyncio.sleep(1)
    print('do some work start 1s')
    # await do_something_else()
    task = asyncio.ensure_future(do_something_else())
    await asyncio.sleep(3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): task is cancelled now")


start = now()
asyncio.run(do_some_work())
print('TIME: ', now() - start)
