def swap_case(s):
    return s.swapcase()
    
words = raw_input("Enter the String:")

if len(words)>0 or len(words)<=1000:
    a = swap_case(words)
    print a
    
else:
    print "Enter the Valid String"
    
