def print_rangoli(size):
    # your code goes here
    for i in range(size):
        print "-"*(size+(i+1))+'c'+"-"*(size+(i+1))

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)