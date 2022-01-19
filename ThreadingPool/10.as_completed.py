from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time


# 参数times用来模拟网络请求的时间
def work(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


def manage():
    task = [executor.submit(work, 3)]
    print('manage is running')
    for i in as_completed(task):  # as_completed only block the thread in loop
        print(f'as completed,return:{i.result()}')
    print('manage is finished')


executor = ThreadPoolExecutor(max_workers=2)
manage()
manage()
