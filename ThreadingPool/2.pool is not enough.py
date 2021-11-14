from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(get_html, (2))
task2 = executor.submit(get_html, (1))
time.sleep(3.1)
print(task1.done())
print(task2.done())
print(task1.result())

#task will be executed one by one
