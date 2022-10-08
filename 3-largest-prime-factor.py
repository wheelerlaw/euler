#!/usr/bin/env python3

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def solution(num):
    # largest = 0
    # factor = num // 2
    # while factor > 1:
    #     if num % factor == 0 and is_prime(factor):
    #         return factor
    #     factor -= 1
    # return num
    largest_factor = 0
    while num != 1:
        factor = 2
        while num % factor > 0 or not is_prime(factor):
            if factor * factor > num:
                factor = num
                break
            factor += 1
        num //= factor
        if factor > largest_factor:
            largest_factor = factor
    return largest_factor


# 5, 7, 13 and 29
# assert solution(58) == 29
# assert solution(13_195) == 29
print(solution(600_851_475_143))


