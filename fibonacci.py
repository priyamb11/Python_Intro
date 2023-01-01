cache = {0: 0, 1: 1}

def fibonacci_of(number):
    if number in cache:
        return cache[number]
    
    cache[number] = fibonacci_of(number - 1) + fibonacci_of(number - 2)
    return cache[number]

print([fibonacci_of(number) for number in range(12)])
print(fibonacci_of(10))
