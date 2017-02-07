N, M = map(int,raw_input().split()) 
for i in xrange(1,N,2): 
    print "-"*(M/2-(3*i-1)/2)+ ".|."*((i-1)/2)+".|." + ".|."*((i-1)/2) + "-"*(M/2-(3*i-1)/2)
print "WELCOME".center(M,"-")
for i in xrange(N-2,-1,-2): 
    print "-"*(M/2-(3*i-1)/2) + ".|."*((i-1)/2)+".|." + ".|."*((i-1)/2) + "-"*(M/2-(3*i-1)/2)