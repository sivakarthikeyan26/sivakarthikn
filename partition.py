print("enter the values")
n,a,b=map(int,input().split(" "))
if n%2==0:
    if a+b==n:
        print("YES")
    elif a+b>n:
        print("NO")
    elif a%2==0 and b%2==0:
        print("no")
    else:
        print("yes")
        
    
else:
    if a+b==n:
        print("YES")
    elif a+b<n:
        print("NO")
    else:
        print("NO")
        
    
        
        
        
