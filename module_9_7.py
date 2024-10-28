def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)
        prime = True
        for i in range(n):
            if i == 1:
                continue
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break
        if not prime:
            print('Простое')
        else:
            print('Составное')
        return n

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
