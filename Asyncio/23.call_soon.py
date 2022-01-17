import asyncio
import functools


def callback(name, stat=1):
    print('args:', name, 'keyword args:', stat)


async def run(loop):
    loop.call_soon(callback, 'get first callback')
    wrapper_func = functools.partial(callback, stat=2)
    loop.call_soon(wrapper_func, 'get second call back')


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run(loop))
finally:
    loop.close()
