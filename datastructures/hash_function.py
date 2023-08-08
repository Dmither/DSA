from collections import Counter
from string import printable

def hash_func(key):
    res = 0
    if isinstance(key, int):
        return key
    for i in range(len(key)):
        res += ((i+1) * ord(key[i])) ** 13
    return res
    

# Підрахунок розподілення хеш-ключів за заданим числом бакетів
def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

# Виведення гістограми результатів (індекс: кількість)
def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■'*count}{padding} ({count})")

print(distribute(printable, 4, hash_func))
plot(distribute(printable, 4, hash_func))