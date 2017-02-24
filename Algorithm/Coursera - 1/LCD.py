
a,b = map(int, raw_input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        c = a%b
        return gcd(b,c)


print gcd(a,b)