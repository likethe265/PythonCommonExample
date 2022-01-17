import asyncio
import functools


def callback(name, stat=1):
    print('args:', name, 'keyword args:', stat)


async def run(loop):
    loop.call_later(2, callback, 'get first callback')
    loop.call_soon(callback, 'callback soon')
    wrapper_func = functools.partial(callback, stat=0)
    loop.call_later(1, wrapper_func, 'get second callback')
    await asyncio.sleep(2)  # 这里如果不设sleep，那么call_soon执行后loop马上退出，导致2个有延时运行的callback也退出了。这里要大于等于delay时间最长的call_later


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run(loop))
finally:
    loop.close()
