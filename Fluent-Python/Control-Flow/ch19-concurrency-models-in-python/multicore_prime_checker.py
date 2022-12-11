import math
import sys
from multiprocessing import Process, SimpleQueue, cpu_count, queues
from time import perf_counter
from typing import NamedTuple


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


NUMBERS = [
    2,
    142702110479723,
    299593572317531,
    3333333333333301,
    3333333333333333,
    3333335652092209,
    4444444444444423,
    4444444444444444,
    4444444488888889,
    5555553133149889,
    5555555555555503,
    5555555555555555,
    6666666666666666,
    6666666666666719,
    6666667141414921,
    7777777536340681,
    7777777777777753,
    7777777777777777,
    9999999999999917,
    9999999999999999,
]


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[PrimeResult]


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))


def start_jobs(procs: int, jobs: JobQueue, results: ResultQueue) -> None:
    for n in NUMBERS:
        jobs.put(n)

    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0)
