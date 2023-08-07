from hash_distribution import plot, distribute
from string import printable
from hash_function import hash_func



plot(distribute(printable, 20, hash_function=hash_func))