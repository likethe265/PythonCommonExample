import asyncio


async def func1(i):
    print(f"协程函数{i}马上开始执行。")
    await asyncio.sleep(2)
    print(f"协程函数{i}执行完毕!")


async def main():
    tasks = []
    for i in range(1, 5):
        # 这里未由协程函数创建协程任务
        tasks.append(func1(i))

    # 注意这里*号。gather自动将函数列表封装成了协程任务。
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
