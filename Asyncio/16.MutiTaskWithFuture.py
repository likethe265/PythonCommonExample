import asyncio
import datetime
import time


def get_time():
    d = datetime.datetime.now()
    return d.strftime('%H:%M:%S')


async def coru_1(future_obj, N):
    print('coru_1 started at:{}'.format(get_time()))
    total = sum(range(N))
    await asyncio.sleep(2)
    future_obj.set_result('coru_1 returns:{}'.format(total))
    print('coru_1 done at:{}'.format(get_time()))


async def coru_2(future_obj, N):
    print('coru_2 started at:{}'.format(get_time()))
    total = sum(range(N))
    await asyncio.sleep(2)
    future_obj.set_result('coru_2 returns:{}'.format(total))
    print('coru_2 done at:{}'.format(get_time()))


def call_back(future_obj):
    time.sleep(1)
    print('saved to redis at :', get_time(), future_obj, future_obj.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    f1 = asyncio.Future()
    f2 = asyncio.Future()
    tasks = [coru_1(f1, 10), coru_2(f2, 20)]
    f1.add_done_callback(call_back)
    f2.add_done_callback(call_back)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
