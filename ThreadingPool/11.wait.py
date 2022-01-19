import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time


# 参数times用来模拟网络请求的时间
def work(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


def manage():
    tasks = [executor.submit(work, 3)]
    print('manage is running0')
    time.sleep(1)
    print('manage is running1')
    time.sleep(1)
    print('manage is running2')
    wait(tasks)
    print(f'manage is finished,result:{tasks[0].result()}')


def infiniteLoop():
    while 1:
        manage()


executor = ThreadPoolExecutor(max_workers=2)
t = threading.Thread(target=infiniteLoop, name='LoopThread')
t.start()
print('loop thread started')
t.join()
