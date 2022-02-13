import asyncio


async def dispatcher():
    for i in range(3):
        await asyncio.sleep(2)
        print('task executed.')


async def runner():
    asyncio.ensure_future(dispatcher(), loop=asyncio.get_event_loop())
    await asyncio.sleep(1)
    print('runner finished')


loop = asyncio.get_event_loop()
loop.run_until_complete(runner())
loop.run_forever()
