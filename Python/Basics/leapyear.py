def is_leap(year):
    # leap = False
    
    # Write your logic here
    if (year >= 1900 and year <= 1000000):
        if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
    else:
        print "Enter the Valid Year Between (1900-10^5)"
        return False
   
if __name__ == '__main__' :
    y = int(raw_input("Enter Year to chk:"))
    chk = is_leap(y)
    print chk
