#!/usr/bin/env python

import asyncio
import websockets


class WebsocketServer:
    def __init__(self):
        self.event = asyncio.Event()

    async def eventGenerator(self):
        while True:
            await asyncio.sleep(2.5)
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
            msg = f'msg from server!'
            await websocket.send(msg)

    async def clientHandler(self, websocket, path):
        try:
            print('new connection...')
            tasks = [self.producer(websocket), self.receive(websocket)]
            await asyncio.gather(*tasks)
        except Exception as e:
            if type(e) == websockets.exceptions.ConnectionClosedError:
                print('client has gone offline')
                await websocket.close()
            else:
                raise e


wss = WebsocketServer()
start_server = websockets.serve(wss.clientHandler, 'localhost', 8989)
tasks = [start_server, wss.eventGenerator()]
try:
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Server crash...")
