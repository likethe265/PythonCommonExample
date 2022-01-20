# coding=utf-8
import asyncio
import functools


def set_event(event):
    print('在回调中设置事件')
    event.set()


async def test(name, event):
    print('\t{} waiting for event'.format(name))
    await event.wait()
    print('\t{} triggered'.format(name))


async def main(loop):
    event = asyncio.Event()
    print('事件开始状态：{}'.format(event.is_set()))
    loop.call_later(1, functools.partial(set_event, event))
    await asyncio.gather(*[test('e1', event), test('e2', event)])
    print('事件结束状态：{}'.format(event.is_set()))
    event.clear()
    print('事件结束状态：{}'.format(event.is_set()))
    print('*' * 50)
    loop.call_later(1, functools.partial(set_event, event))
    await asyncio.gather(*[test('e1', event), test('e2', event)])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:  # -------------------------------
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
