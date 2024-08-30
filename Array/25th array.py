a=int(input("enter a number="))
arr=[]
result = []
    
zerocount = 0 #Count number of zeros
for i in range(a):
    b=int(input("enter b num="))
    arr.append(b)
    
for num in arr:
    if(num==0):
        zerocount += 1
    else:
        result.append(num)
        
result.extend([0] * zerocount)
    
for i in range(len(arr)):
    arr[i] = result[i]
    print(arr[i])

