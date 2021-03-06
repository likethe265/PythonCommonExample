import asyncio
import random


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)
        # queue.task_done()   # indicate complete task


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await asyncio.sleep(1)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))


async def main():
    queue = asyncio.Queue()

    producer_1 = producer(queue, 'producer_1')
    consumer_1 = consumer(queue, 'consumer_1')
    await asyncio.gather(*[producer_1, consumer_1], return_exceptions=True)
    await queue.join()  # wait until the consumer has processed all items
    consumer_1.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
