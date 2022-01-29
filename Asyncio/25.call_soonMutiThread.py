import asyncio
import time
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    print("start loop")
    loop.run_forever()


def more_work(x):
    print('start work {}'.format(x))
    time.sleep(x)
    print('Finished work {}'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

new_loop.call_soon_threadsafe(more_work, 3)
print('3')
new_loop.call_soon_threadsafe(more_work, 2)
print('2')