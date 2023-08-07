def hash_func(key):
    res = sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    )
    while (res < 100_000_000_000):
        res *= ord(repr(key).lstrip("'")[0])
    return res
    

print(hash_func("Lorem"))
print(hash_func("Loren"))
print(hash_func("Loreo"))