import asyncio
import datetime


def get_time():
    d = datetime.datetime.now()
    return d.strftime('%H:%M:%S')


# async 定义了mytask为协程对象
async def mytask(task_id):
    # 这里就像gevent的sleep方法模拟IO，而且该协程会被asyncio自动切换
    print('task-{} started at:{}'.format(task_id, get_time()))
    await asyncio.sleep(1)  # await 要求该行语句的IO是有返回值的例如response=request.get(url)，如果直接使用await time.sleep(2),则无法创建协程对象
    print('task-{} done at:{}'.format(task_id, get_time()))


# 创建事件循环对象，该事件循环由当前主线程拥有
loop = asyncio.get_event_loop()
tasks = [mytask(i) for i in range(4)]  # 这里mytask()是协程对象，不会离开运行。
loop.run_until_complete(asyncio.wait(tasks))  # 这里实行的逻辑就像gevent.joinall(tasks)一样，表示loop一直运行直到所有的协程tasks都完成
