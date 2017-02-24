# Problem Description
# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
# Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
# Output Format. Output GCD(𝑎, 𝑏).
# Time Limits.
# language C C++ Java Python C# Haskell JavaScript Ruby Scala
# time (sec) 1 1 1.5 5 1.5 2 5 5 3
# Memory Limit. 512MB.
# Sample 1.






a,b = map(int, raw_input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        c = a%b
        return gcd(b,c)


print gcd(a,b)