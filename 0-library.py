#!/usr/bin/env python3

def arithmatic_sum(num, divisor=1):
    i = num // divisor
    return divisor * (i * (i+1) // 2)
