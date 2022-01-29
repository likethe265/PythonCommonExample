# -*- coding:utf-8 -*-
import asyncio


async def func1(i):
    print(f"协程函数{i}马上开始执行。")
    await asyncio.sleep(i)
    return i


async def main():
    tasks = []
    for i in range(1, 5):
        tasks.append(func1(i))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"执行结果: {result}")


if __name__ == '__main__':
    asyncio.run(main())
