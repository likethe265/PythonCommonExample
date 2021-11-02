import asyncio
import contextlib
import time

now = lambda: time.time()


async def do_something_else():
    i = 0
    while i <= 3:
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do something else {}'.format(currentTime, i))
        await asyncio.sleep(1)
        i += 1


async def do_some_work():
    i = 0
    while i <= 10:
        await asyncio.sleep(1)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do some work {}'.format(currentTime, i))
        if i == 3:
            # await do_something_else()
            asyncio.ensure_future(do_something_else())
        i += 1


start = now()

loop = asyncio.get_event_loop()
coroutine = do_some_work()
task = asyncio.ensure_future(coroutine)
# loop.run_forever()
try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    all_tasks = asyncio.gather(*asyncio.all_tasks(loop), return_exceptions=True)
    all_tasks.cancel()
    with contextlib.suppress(asyncio.CancelledError):
        loop.run_until_complete(all_tasks)
    loop.run_until_complete(loop.shutdown_asyncgens())
finally:
    loop.close()

print('TIME: ', now() - start)
