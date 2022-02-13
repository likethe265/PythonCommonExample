#!/usr/bin/env python

import asyncio
import random
import websockets


class WebsocketClient:
    def __init__(self):
        self.clientID = random.randint(0, 100)
        self.curretConnection = None

    async def clientMsgGenerator(self):
        while True:
            await asyncio.sleep(1.5)
            if self.curretConnection:
                msg = f'msg from client:{self.clientID}!'
                asyncio.ensure_future(self.curretConnection.send(msg))

    async def consumer(self, message):
        print(f'server rec:{message}')

    async def receive(self, websocket):
        while True:
            msg = await websocket.recv()
            print(f'server rec:{msg}')

    async def connectToServer(self):
        while True:
            try:
                async with websockets.connect('ws://localhost:8989') as websocket:
                    self.curretConnection = websocket
                    await self.receive(websocket)
            except Exception as e:
                self.curretConnection = None
                if type(e) == ConnectionRefusedError or type(e) == websockets.exceptions.ConnectionClosedError:
                    print('Client is waiting for server launching...')
                    await asyncio.sleep(5)
                else:
                    raise e


wsc = WebsocketClient()
tasks = [wsc.connectToServer(), wsc.clientMsgGenerator()]
try:
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    print("Client crash...")
