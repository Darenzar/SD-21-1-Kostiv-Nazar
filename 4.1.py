def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_num_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


prime = prime_num_generator()
if __name__ == "__main__":
    for i in range(10):
        print(next(prime))
