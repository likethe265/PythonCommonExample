#!/usr/bin/env python

import asyncio
import websockets


class WebsocketServer:
    def __init__(self):
        self.currentConnections = []

    async def serverMsgGenerator(self):
        '''producer may not in same thread, so we use ensure_future to create task in async loop'''
        while True:
            await asyncio.sleep(2.5)
            for ws in self.currentConnections:
                asyncio.ensure_future(ws.send('msg from server'))

    async def receive(self, websocket):
        while True:
            msg = await websocket.recv()
            print(f'server rec:{msg}')

    async def clientHandler(self, websocket, path):
        try:
            print('new connection...')
            self.currentConnections.append(websocket)
            await self.receive(websocket)
        except Exception as e:
            self.currentConnections.remove(websocket)
            if type(e) == websockets.exceptions.ConnectionClosedError:
                print('client has gone offline')
                await websocket.close()
            else:
                raise e


wss = WebsocketServer()
start_server = websockets.serve(wss.clientHandler, 'localhost', 8989)
tasks = [start_server, wss.serverMsgGenerator()]
try:
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Server crash...")
