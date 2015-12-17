
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=2)


def sleep_fun():
    import time
    print 'sleep start'
    time.sleep(5)
    print 'sleep end'

def no_sleep():
    print 'no sleep'


if __name__ == '__main__':
    executor.submit(sleep_fun)
    no_sleep()
