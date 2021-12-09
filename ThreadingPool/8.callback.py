from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times, a, b, callback_fn, *args):
    time.sleep(times)
    print(a + b)
    print("get page {}s finished".format(times))
    callback_fn(*args)
    return times


def callback_fn(*args):
    print(args)
    print('this is callback function')


executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(get_html, 2, 100, 101, callback_fn, 1, 2, 3)
print(task1.result())
