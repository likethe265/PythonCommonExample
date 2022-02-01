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


async def consumer(websocket):
    print('server starts to wait producer...')
    while 1:
        var = await queue.get()
        print(f'get {var}')
        t_serv_rec = str(time.time())
        payload = json.dumps((var, t_serv_rec))
        await websocket.send(payload)


async def echo(websocket, path):
    name = await websocket.recv()
    tasks = [producer(), consumer(websocket)]
    asyncio.gather(*tasks, return_exceptions=True)


start_server = websockets.serve(echo, 'localhost', 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
