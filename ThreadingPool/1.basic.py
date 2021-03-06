from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times, info):
    time.sleep(times)
    print(info)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(get_html, 2, 'task1')
task2 = executor.submit(get_html, 1, 'task2')
# done方法用于判定某个任务是否完成
print(task1.done())
# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
print(task2.cancel())
time.sleep(3)
print(task1.done())
print(task2.done())  # still print done because it has been cancelled
# result方法可以获取task的执行结果, 阻塞调用
print(task1.result())
