#!/usr/bin/env python

import asyncio
import json
import time

import websockets


async def hello():
    async with websockets.connect('ws://localhost:8888') as websocket:
        name = 'testMsg'
        t_startSend = time.time()
        await websocket.send(str(t_startSend))
        t_finishSend = time.time()

        payload = await websocket.recv()
        serverReply = json.loads(payload)
        serverReplyContent = float(serverReply[0])
        t_serv_rec = float(serverReply[1])
        print(f'send to server cost:{t_serv_rec - t_startSend} recv from server cost:{t_serv_rec - t_finishSend}')


asyncio.get_event_loop().run_until_complete(hello())
