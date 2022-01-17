import asyncio
import datetime


def get_time():
    d = datetime.datetime.now()
    return d.strftime('%M:%S')


async def coro(group_id, coro_id):
    print('group{}-task{} started at:{}'.format(group_id, coro_id, get_time()))
    await asyncio.sleep(coro_id)  # 模拟读取文件的耗时IO
    return 'group{}-task{} done at:{}'.format(group_id, coro_id, get_time())


loop = asyncio.get_event_loop()

# 创建三组tasks
tasks1 = [asyncio.ensure_future(coro(1, i)) for i in range(1, 5)]
tasks2 = [asyncio.ensure_future(coro(2, i)) for i in range(5, 6)]
tasks3 = [asyncio.ensure_future(coro(3, i)) for i in range(7, 10)]

group1 = asyncio.gather(*tasks1)  # 对第1组的协程进行分组，group1
group2 = asyncio.gather(*tasks2)  # 对第2组的协程进行分组，group2
group3 = asyncio.gather(*tasks3)  # 对第3组的协程进行分组，group3

all_groups = asyncio.gather(group1, group2, group3)  # 把3个group再聚合成一个大组，也是就所有协程对象的被聚合到一个大组

loop = asyncio.get_event_loop()
all_group_result = loop.run_until_complete(all_groups)
for index, group in enumerate(all_group_result):  # 获取每组协程的输出
    print('group {} result:{}'.format(index + 1, group))
loop.close()
