import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_num_getter():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def time_wrapper(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(t2-t1)
        return result
    return wrapper


@time_wrapper
def gen():
    prime = prime_num_getter()
    for i in range(10):
        print(next(prime))


if __name__ == "__main__":
    gen()

