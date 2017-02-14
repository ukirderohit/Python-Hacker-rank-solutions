def count_substring(string, sub_string):
    
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            c+=1
    print c


if __name__ == '__main__':
    global coun
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count_substring(string, sub_string)
    