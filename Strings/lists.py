if __name__ == '__main__':
    N = int(raw_input())
    li  = []
    for i in range(1,N+1):
        
        s = raw_input().split(' ')
       
        if s[0]=="insert":
            li.insert(int(s[1]),int(s[2]))
        if s[0]=="print":
            print li
        if s[0]=="remove":
            li.remove(int(s[1])) 
        if s[0]=="append":
            li.append(int(s[1]))
        if s[0]=="sort":
            li.sort()
        if s[0]=="pop":
            li.pop()
        if s[0]=="reverse":
            li.reverse()
        
            
        