from proj import task
from celery import group, chain
import time

add = task.add
mul = task.mul

def main():
    """
    celery -A proj worker -Q hipri,celery
    """
    add.delay(2, 2)
    add.apply_async((2, 3), queue='queue1', countdown=10)
    sub_task = add.subtask((9, 8))
    sub_task.delay()
    sub_task.delay()
    sub_task2 = add.s(9, 9)
    res2 = sub_task2.delay()
    start = time.time()
    try:
        print(res2.get(0.5))
    except Exception as e:
        print(e)
        print(time.time()-start)
    
    g = group(add.s(i) for i in range(10))
    print(g(2).get())
    c = chain(add.s(4, 4) | mul.s(8))
    print(c().get())

if __name__ == '__main__':
    main()
