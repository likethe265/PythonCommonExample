import asyncio
import datetime


def get_time():
    d = datetime.datetime.now()
    return d.strftime('%H:%M:%S')


async def read_file(task_id):
    print('task-{} started at:{}'.format(task_id, get_time()))
    await asyncio.sleep(2)  # 模拟读取文件的耗时IO
    return 'task-{} done at:{}'.format(task_id, get_time())


loop = asyncio.get_event_loop()
coros = [read_file(i) for i in range(5)]  # 创建多个协程
tasks = [asyncio.ensure_future(coro) for coro in coros]  # 将协程封装为task对象
loop.run_until_complete(asyncio.wait(tasks))
# 或者loop.run_until_complete(asyncio.gether(*tasks))

# 重点在这里，当所有的协程结束后，可批量获取所有协程的返回结果
get_all_result = [t.result() for t in tasks]
print(get_all_result)
