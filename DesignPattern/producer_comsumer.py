import asyncio


class ConsumerProducerModel:
    def __init__(self, producer, consumer, queue=asyncio.Queue(), plate_size=6):  # the plate holds 6pcs bread
        self.queue = queue
        self.producer = producer
        self.consumer = consumer
        self.plate_size = plate_size

    async def produce_bread(self):
        for i in range(self.plate_size):
            bread = f"bread {i}"
            await asyncio.sleep(0.5)  # bread makes faster, 0.5s/pc
            await self.queue.put(bread)
            print(f'{self.producer} makes {bread}')

    async def consume_bread(self):
        while True:
            bread = await self.queue.get()
            await asyncio.sleep(1)  # eat slower, 1s/pc
            print(f'{self.consumer} eats {bread}')
            self.queue.task_done()


async def main():
    queue = asyncio.Queue()
    cp1 = ConsumerProducerModel("John", "Grace", queue)  # group 1
    cp2 = ConsumerProducerModel("Mike", "Lucy", queue)  # group 2

    producer_1 = cp1.produce_bread()
    producer_2 = cp2.produce_bread()

    consumer_1 = asyncio.ensure_future(cp1.consume_bread())
    consumer_2 = asyncio.ensure_future(cp2.consume_bread())

    await asyncio.gather(*[producer_1, producer_2])
    await queue.join()
    consumer_1.cancel()
    consumer_2.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
