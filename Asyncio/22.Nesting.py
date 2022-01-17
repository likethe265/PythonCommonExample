import asyncio
import datetime


def get_time():
    d = datetime.datetime.now()
    return d.strftime('%H:%M:%S')


async def inner_coro(task_id):
    print('coro-{} started at:{}'.format(task_id, get_time()))
    await asyncio.sleep(5)  # 模拟读取文件的耗时IO
    return 'coro-{} done at:{}'.format(task_id, get_time())


async def outter_coro():
    print('outter_coro started at:{}'.format(get_time()))
    coros = [inner_coro(i) for i in range(4)]
    tasks = [asyncio.ensure_future(coro) for coro in coros]
    inner_tasks, pendings = await asyncio.wait(tasks)  # 这句实现了协程中再调用协程
    print('outter_coro done at:{}'.format(get_time()))
    # 使用asyncio.wait(tasks)可以在外层协程里面获取嵌套协程的运行返回值
    for task in inner_tasks:
        print(task.result())


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(outter_coro())
except Exception as e:
    loop.close()
