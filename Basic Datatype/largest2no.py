if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    print arr
    for i in range(n):
        if arr[i]!=arr[i+1]:
            print arr[i+1]
            break;
        
        