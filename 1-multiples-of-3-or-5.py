#!/usr/bin/env python3
import math


def solution(num):
    sum_ = 0
    for i in range(math.ceil(num / 3)):
        sum_ += i * 3
    for i in range(math.ceil(num / 5)):
        sum_ += i * 5
    for i in range(math.ceil(num / 15)):
        sum_ -= i * 15
    return sum_


assert solution(10) == 23
assert solution(16) == 60
print(solution(1000))


def arithmatic_sum(num, divisor=1):
    i = num // divisor
    return divisor * (i * (i+1) // 2)


def better_solution(num):
    return arithmatic_sum(num - 1, 3) + arithmatic_sum(num - 1, 5) - arithmatic_sum(num - 1, 15)


assert arithmatic_sum(10, 3) == 18
assert better_solution(10) == 23
assert better_solution(16) == 60
assert solution(1_000) == better_solution(1_000)
