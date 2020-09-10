from threading import Thread
from multiprocessing import Pool
from timeit import default_timer

def workload():
    """
    provide CPU pound workload
    """
    counter = 1000000
    while counter > 0:
        counter -= 1

settings = [2 ** i for i in range(9)]

def serializing(n):
    """
    workloading one by one/serially
    """
    start = default_timer()

    for _ in range(n):
        workload()
    return (default_timer() - start)

def threading(n):
    """
    dispatch workload to n thread
    """
    start = default_timer()

    thread_pool = []
    for _ in range(n):
        t = Thread(target=workload, args=())
        t.start()
        thread_pool.append(t)
    for t in thread_pool:
        t.join()
    return (default_timer() - start)

def multiprocessing(n):
    """
    dispatch workload to n process
    """

    start = default_timer()

    process_pool = Pool(processes=n, )
    process_pool.apply(workload)
    process_pool.close()
    process_pool.join()
    return (default_timer() - start)

if __name__ == '__main__':
    print("Bench mark result:")
    print("serial", serializing(256))
    print("thread", threading(256))
    print("multi process", multiprocessing(256))
