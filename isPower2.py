#Given an integer, write a function to determine if it is a power of two.


def isPower(n):
    # Base case
    if (n <= 1):
        return True

    # Try all numbers from 2 to sqrt(n)
    # as base
    for x in range(2, (int)(math.sqrt(n)) + 1):
        p = x

        # Keep multiplying p with x while
        # is smaller than or equal to x
        while (p <= n):
            p = p * x

            if (p == n):
                return True

    return False

print isPower(8)
