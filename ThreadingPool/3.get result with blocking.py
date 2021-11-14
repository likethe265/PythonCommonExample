from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
start = time.time()
task1 = executor.submit(get_html, (2))
task2 = executor.submit(get_html, (1))
print(task1.result())
print(f'time from start on task1：{time.time() - start}')
print(task2.result())
print(f'time from start on task2：{time.time() - start}')

# task will be executed one by one
