"""
双向队列
"""
"""
queue
    提供了同步（线程安全）类Queue、LifoQueue和PriorityQueue，不同的线程可以利用这些数据类型来交换信息。
multiprocessing
    这个包实现了自己的Queue，它跟queue.Queue类似，是设计给进程间通信用的。同时还有一个专门的multiprocessing.JoinableQueue类型，可以让任务管理变得更方便。
asyncio
    里面有Queue、LifoQueue、PriorityQueue和JoinableQueue，这些类受到queue和multiprocessing模块的影响，但是为异步编程里的任务管理提供了专门的便利。
heapq
    heapq没有队列类，而是提供了heappush和heappop方法，让用户可以把可变序列当作堆队列或者优先队列来使用。
"""

from collections import deque

if __name__ == '__main__':

    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)
