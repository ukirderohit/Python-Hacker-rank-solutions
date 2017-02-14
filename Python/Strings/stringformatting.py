#Read N
N=int(raw_input())
#Set required width as necessary(the -2), I prefer the total width
#The total width looks better actually
width=len(bin(N))-2
#Required range
for num in range(1,N+1):
	#Printing number in required bases
    for base in 'doXb':
    	#Curly braces makes it look like angularjs lol
        #Read .format python docs
        #An example has just this in it and explains quite well
        print '{0:{width}{base}}'.format(num,base=base,width=width),
    print