for i in range(int(raw_input())):   
    a = int(raw_input()); 
    A = set(raw_input().split())
    b = int(raw_input()); 
    B = set(raw_input().split())
    if B.intersection(A) == A:
        print True
    else
        print False