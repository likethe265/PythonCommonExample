import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# the result 'balance' is different in every run
# 由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
#
# 初始值
# balance = 0
#
# t1: x1 = balance + 5  # x1 = 0 + 5 = 5
# t1: balance = x1  # balance = 5
# t1: x1 = balance - 5  # x1 = 5 - 5 = 0
# t1: balance = x1  # balance = 0
#
# t2: x2 = balance + 8  # x2 = 0 + 8 = 8
# t2: balance = x2  # balance = 8
# t2: x2 = balance - 8  # x2 = 8 - 8 = 0
# t2: balance = x2  # balance = 0
#
# 结果
# balance = 0
# 但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
#
# 初始值
# balance = 0
#
# t1: x1 = balance + 5  # x1 = 0 + 5 = 5
#
# t2: x2 = balance + 8  # x2 = 0 + 8 = 8
# t2: balance = x2  # balance = 8
#
# t1: balance = x1  # balance = 5
# t1: x1 = balance - 5  # x1 = 5 - 5 = 0
# t1: balance = x1  # balance = 0
#
# t2: x2 = balance - 8  # x2 = 0 - 8 = -8
# t2: balance = x2  # balance = -8
#
# 结果
# balance = -8