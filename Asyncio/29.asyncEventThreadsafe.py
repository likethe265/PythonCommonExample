import asyncio
from threading import Thread


class Event_ts(asyncio.Event):
    # TODO: clear() method
    def set(self):
        self._loop.call_soon_threadsafe(super().set)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def producer(event):
    while True:
        print('producer emit signal')
        event.set()
        await asyncio.sleep(1)


async def consumer(event):
    while True:
        await event.wait()
        event.clear()
        print('consumer get signal')


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
e = Event_ts()
asyncio.run_coroutine_threadsafe(producer(e), new_loop)
asyncio.get_event_loop().run_until_complete(consumer(e))
