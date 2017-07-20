import time
from lib.time_tracker import TimeTracker

class Logger:
    def log(self, message):
        print('[TimeTracking] {function_name} {args} {kwargs} - total: {total_time:3.6f} s - partial: {partial_time:3.6f} s'.format(**message))

logger = Logger()
time_tracker = TimeTracker(logger, True)

@time_tracker.time_track()
def boo(x, y):
    time.sleep(0.2)
    return dodo(x, 0.3) + dodo(y, 0.4)

@time_tracker.time_track()
def dodo(x, i):
    time.sleep(i)
    return x

boo(1, 2)

@time_tracker.time_track()
def f(x, i):
    time.sleep(0.1)
    if i == 0:
        return x
    else:
        return 3 * g(x, i) + 1

@time_tracker.time_track()
def g(x, i):
    time.sleep(0.3)
    res = f(x-1, i-1) / 2
    time.sleep(0.4)
    return res

f(1, 2)

@time_tracker.time_track()
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(5)

@time_tracker.time_track()
def error_fun():
    time.sleep(0.2)
    raise Exception('Booo')

@time_tracker.time_track()
def error_fun_caller():
    time.sleep(0.1)
    error_fun()

try:
    error_fun_caller()
except:
    pass
