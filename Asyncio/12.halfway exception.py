import asyncio
import contextlib
import time

now = lambda: time.time()


async def do_something_else():
    i = 0
    while i <= 5:
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do something else {}'.format(currentTime, i))
        await asyncio.sleep(0.5)
        i += 1


async def do_some_work():
    i = 0
    try:
        while i <= 10:
            await asyncio.sleep(0.5)
            currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print('{}   do some work {}'.format(currentTime, i))
            if i == 2:
                asyncio.ensure_future(do_something_else())
            if i == 3:
                raise Exception('user exception')
            i += 1
    except Exception as e:
        print(e)  # do something else will hanged when exception happens. There's some delay to kill the coroutine.


start = now()
asyncio.run(do_some_work())
print('TIME: ', now() - start)
