# coding=utf-8
import asyncio
import functools


async def set_event(event):
    while 1:
        event.set()
        event.clear()
        await asyncio.sleep(2)


async def test(name, event):
    while 1:
        await event.wait()
        print('\t{} triggered'.format(name))


async def main(loop):
    event = asyncio.Event()
    await asyncio.gather(*[test('e1', event), test('e2', event), set_event(event)])
    print('this print should not be called')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:  # -------------------------------
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
