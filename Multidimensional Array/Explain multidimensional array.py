r=int(input("enter a row="))
c=int(input("enter a col="))
n=[] 
for i in range(0,r):#row=given 2 inputs  n[i]
    m=[]

    
    for j in range(0,c):#col=2inputs only
        b=int(input("value="))# => two box ikumey ithula thaa input vanganum.
                                        #bcoz of loop kula iruku 2iku apply agum  n[j]
        m.append(b)#m inner box =>col=2
    n.append(m)
print(n)


#explain 
for i in range(0,r):
    for j in range(0,c):
        print(n[i][j],end=" ")#positions
    print()


#n=[(m) (m) ]=>outer box
    
#row-2
#col-2







'''[1,2,3]
[6,7,8]
[[1,2,3],[6,7,8]]'''
