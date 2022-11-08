import math

# Check if a number is Prime


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


print(is_prime(5_000_111_000_222_021))
