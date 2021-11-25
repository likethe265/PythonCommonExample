import signal
import sys
import queue
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED


def exit_threads(executor):
    print('\nWrapping up, please wait...')

    py_version = sys.version_info
    if (py_version.major == 3) and (py_version.minor < 9):
        # py versions less than 3.9
        # Executor#shutdown does not accept
        # cancel_futures keyword
        # manually shutdown
        # code taken from https://github.com/python/cpython/blob/3.9/Lib/concurrent/futures/thread.py#L210

        # prevent new tasks from being submitted
        executor.shutdown(wait=False)
        while True:
            # cancel all waiting tasks
            try:
                work_item = executor._work_queue.get_nowait()

            except queue.Empty:
                break

            if work_item is not None:
                work_item.future.cancel()

    else:
        executor.shutdown(cancel_futures=True)

    sys.exit(0)


def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=5)
# comment this below will trigger keyboard interrupt
signal.signal(
    signal.SIGINT,
    lambda sig, frame: exit_threads(executor)
)

# run desired code here...
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
