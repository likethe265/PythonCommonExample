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
        print(f'client rec:{message}')

    async def producer(self, websocket):
        await self.event.wait()
        self.event.clear()
        return f'msg from client:{self.clientID}!'

    async def connectToServer(self):
        while True:
            try:
                async with websockets.connect('ws://localhost:8989') as websocket:
                    while True:
                        listener_task = asyncio.ensure_future(websocket.recv())
                        producer_task = asyncio.ensure_future(self.producer(websocket))
                        done, pending = await asyncio.wait(
                            [listener_task, producer_task],
                            return_when=asyncio.FIRST_COMPLETED)

                        if listener_task in done:
                            message = listener_task.result()
                            await self.consumer(message)
                        else:
                            listener_task.cancel()

                        if producer_task in done:
                            message = producer_task.result()
                            await websocket.send(message)
                        else:
                            producer_task.cancel()
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
