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

    async def producer(self, websocket):
        await self.event.wait()
        self.event.clear()
        return f'msg from server!'

    async def clientHandler(self, websocket, path):
        try:
            print('new connection...')
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
            if type(e) == websockets.exceptions.ConnectionClosedError:
                print('client has gone offline')
                await websocket.close()
            else:
                raise e

    async def clientHandlerWrapper(self, websocket, path):
        tasks = [self.clientHandler(websocket, path), self.eventGenerator()]
        await asyncio.gather(*tasks)


wss = WebsocketServer()
start_server = websockets.serve(wss.clientHandler, 'localhost', 8989)
tasks = [start_server, wss.eventGenerator()]
try:
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Server crash...")
