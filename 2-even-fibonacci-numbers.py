#!/usr/bin/env python3

def solution(num):
    curr = 1
    prev = 0
    sum_ = 0
    while curr <= num:
        if curr % 2 == 0:
            sum_ += curr
        next_ = prev + curr
        prev = curr
        curr = next_

    return sum_


assert solution(50) == 44
assert solution(317812) == 257114
print(solution(4_000_000))


# def E(n):
#     if n == 0: return 2
#     if n == 1: return 8
#     return 4*E(n-1)+E(n-2)
#
# print(E(10))
# print(E(3))
# print(E(4_000_000))

# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def better_solution(num):
    sum_ = 0
    prev = 1
    curr = 1
    next_ = prev + curr
    while next_ < num:
        sum_ += next_
        prev = next_ + curr
        curr = next_ + prev
        next_ = prev + curr

    return sum_


assert better_solution(4_000_000) == solution(4_000_000)
