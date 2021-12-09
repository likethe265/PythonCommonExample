from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]  # 并不是真的url
all_task = [executor.submit(get_html, url) for url in urls]

for future in as_completed(all_task):
    print(f'{future} finished')

# as_completed() will yield return all the futures in the task.
# Task will be returned as long as finished and then continue to block to wait the rest unfinished tasks.
