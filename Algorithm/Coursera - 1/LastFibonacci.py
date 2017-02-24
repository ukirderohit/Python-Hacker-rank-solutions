# Problem Description
# Task. Given an integer ??, find the ??th Fibonacci number ????.
# Input Format. The input consists of a single integer ??.
# Constraints. 0 = ?? = 45.
# Output Format. Output ????.
# Time Limits.
# language C C++ Java Python C# Haskell JavaScript Ruby Scala
# time (sec) 1 1 1.5 5 1.5 2 5 5 3
# Memory Limit. 512MB.





n = int(raw_input())

def fibo(n):
    if n<=1:
        return n
    else:
        previous = 0
        current = 1
        for _ in range(n-1):
            previous, current = current, previous+current
        return current%10
        


print fibo(n)