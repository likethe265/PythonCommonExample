import asyncio


async def func1(i):
    print(f"协程函数{i}马上开始执行。")
    await asyncio.sleep(2)
    print(f"协程函数{i}执行完毕!")


async def main():
    tasks = []
    # 创建包含4个协程任务的列表
    for i in range(1, 5):
        tasks.append(asyncio.create_task(func1(i)))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())