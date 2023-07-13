#!/usr/bin/env python3
""" Minimum Operations """
def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    else:
        i = 2
        count = 0
        while i <= n:
            if n % i == 0:
                count += i
                n = n / i
            else:
                i += 1
        return count

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))