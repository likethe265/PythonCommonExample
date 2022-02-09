#!/usr/bin/env python

import asyncio
import random
import websockets


class WebsocketClient:
    def __init__(self):
        self.clientID = random.randint(0, 100)
        self.event = asyncio.Event()

    async def eventGenerator(self):
        while True:
            await asyncio.sleep(1.5)
            self.event.set()

    async def consumer(self, message):
        print(f'server rec:{message}')

    async def receive(self, websocket):
        while True:
            msg = await websocket.recv()
            await self.consumer(msg)

    async def producer(self, websocket):
        while True:
            await self.event.wait()
            self.event.clear()
            msg = f'msg from client:{self.clientID}!'
            await websocket.send(msg)

    async def connectToServer(self):
        while True:
            try:
                async with websockets.connect('ws://localhost:8989') as websocket:
                    tasks = [self.producer(websocket), self.receive(websocket)]
                    await asyncio.gather(*tasks)
            except Exception as e:
                if type(e) == ConnectionRefusedError or type(e) == websockets.exceptions.ConnectionClosedError:
                    print('Client is waiting for server launching...')
                    await asyncio.sleep(5)
                else:
                    raise e


wsc = WebsocketClient()
tasks = [wsc.connectToServer(), wsc.eventGenerator()]
try:
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    print("Client crash...")
