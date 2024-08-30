a = int(input("Enter elements= "))
arr = []
for i in range(a):
    b = int(input("Enter value= "))
    arr.append(b)
print(arr)

if(len(arr)>0): #Find leaders
    maxright = arr[-1]#arr-1 Start last element as the first leader
    print(maxright,end=' ')#4
    
    
for i in range(len(arr)-2,-1,-1):#array from second last to the first
    if(arr[i]> maxright):
        maxright = arr[i]
        print(maxright,end=' ')
        
        
       
