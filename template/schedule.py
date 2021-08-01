import sched
import time

s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.asctime(), a)


def print_some_times():
    print("setting time", time.asctime())
    s.enter(10, 1, print_time)
    s.enter(20, 2, print_time, argument=('positional',))
    s.enter(30, 1, print_time, kwargs={'a': 'keyword'})

    print("start time", time.asctime())
    s.run()
    print("test")


print_some_times()
print("finished time ", time.asctime())
