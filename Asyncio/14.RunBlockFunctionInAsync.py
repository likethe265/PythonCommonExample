from concurrent.futures import ThreadPoolExecutor
import asyncio, time


def blockFunction():
    time.sleep(3)
    printThreadName()
    return "blockFunction after 3s"


async def asyncWaitFunction():
    await asyncio.sleep(1)
    printThreadName()
    return "asyncWaitFunction after 1s"


async def returnfuture():
    loop = asyncio.get_event_loop()
    newexecutor = ThreadPoolExecutor()
    future1 = loop.run_in_executor(newexecutor, blockFunction)
    future2 = asyncWaitFunction()
    results = await asyncio.gather(*[future1, future2])
    for r in results:
        print(r)


def printThreadName():
    import threading
    print("Current thread name:", threading.current_thread())


asyncio.run(returnfuture())
