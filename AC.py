from collections import deque

num = int(input())

for _ in range(num):
    orders = str(input()) 
    n = int(input()) 
    p = list(input()[1:-1].split(','))   
    d = deque(p)    
    
    if n == 0:   
        d = deque([])
    
    boolean = False 
    
    for i in orders:
        if 'D' == i:
            if len(d) == 0:    
                print("error")
                break
            if boolean:    
                d.pop()
            else:           
                d.popleft()
        else:
            if boolean:      
                boolean = False
            else:
                boolean = True
    else:
        d = list(d)
        if boolean:    
            d.reverse()
        print("[" + ",".join(d) + "]")