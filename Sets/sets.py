def average(array):
    # your code goes here
    distinctht = set(array)
    # print distinctht
    tot = len(distinctht)
    
    sum1 = sum([float(x) for x in distinctht])
    # print sum1
    # print tot
    return float(sum1/tot)
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result