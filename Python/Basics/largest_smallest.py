largest = None
smallest = None
while True:
    
    
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        n = int(num)
        
        if (n < smallest or smallest==None):
            smallest = n
        else:
            smallest = smallest
        if (n > largest or largest==None):
            largest = n
        else:
            largest=largest
    except:
        print "Invalid input"
    
print "Maximum is", largest
print "Minimum is", smallest

