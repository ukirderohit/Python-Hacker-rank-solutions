q = int(raw_input().strip())
for a0 in xrange(q):
    s=raw_input().strip()
    # if s.startswith('0'):
        # print "No"
    # print s.find('1')
    # print s.rfind(s,a0,a0-1)
    # posof1 = s.find('1')
    digits = [str(x) for x in str(s)]
    print digits
    for digit in len(digits):
        if digits[digit]-digits[digit-1] == 1:
            print "yes"
            