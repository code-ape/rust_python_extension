import sys
import timeit

sys.path.append("./target/release")

from librust_python_example import fib as rust_fib


def python_fib(fib_num):
    if fib_num < 2:
        return 1
    prev1 = 1
    prev2 = 1
    new = 0

    for i in xrange(fib_num):
        new = prev1 + prev2
        prev2 = prev1
        prev1 = new

    return prev1


# make sure both perform the fib function correctly
num = 30

rust_res = rust_fib(num)
print("rust fib({0}) = {1}".format(num, rust_res))

python_res = python_fib(num)
print("python fib({0}) = {1}".format(num, python_res))


# use timeit to measure the performance of both
iterations = 100000
rust_total_time = timeit.timeit('rust_fib({0})'.format(
    num), setup="""
from __main__ import rust_fib
gc.enable()
""", number=iterations)

rust_average_time = rust_total_time / iterations


python_total_time = timeit.timeit('python_fib({0})'.format(
    num), setup="""
from __main__ import python_fib
gc.enable()
""", number=iterations)

python_average_time = python_total_time / iterations


# print results from benchmark
print("rust fib({0}) average time: {1}".format(num, rust_average_time))
print("python fib({0}) average time: {1}".format(num, python_average_time))
print("rust speedup factor = {0}".format(
    python_average_time / rust_average_time))


print("Done!")
