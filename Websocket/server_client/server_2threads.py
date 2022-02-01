#!/usr/bin/env python

import asyncio
import json
import threading
import time

import websockets

queue = asyncio.Queue()
new_loop = asyncio.new_event_loop()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def producer():
    for i in range(5):
        await asyncio.sleep(1)
        queue.put_nowait(i)
        print(f'put {i}')


async def echo(websocket, path):
    name = await websocket.recv()
    asyncio.run_coroutine_threadsafe(producer(), new_loop)
    print('server starts to wait producer...')
    while 1:
        var = await queue.get()
        print(f'get {var}')
        t_serv_rec = str(time.time())
        payload = json.dumps((var, t_serv_rec))
        await websocket.send(payload)


start_server = websockets.serve(echo, 'localhost', 8888)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


t = threading.Thread(target=start_loop, args=(new_loop,))
t.start()
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
