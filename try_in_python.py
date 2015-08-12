import sys

sys.path.append("./target/release")

from librust_python_example import fib

num = 30
res = fib(num)
print("fib({0}) = {1}".format(num, res))

print("done!")
