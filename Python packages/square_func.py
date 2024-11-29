def square(num):
    sqrt=0;
    for i in range(1,num,1):
        if(num%i==0):
            if(i*i==num):
                sqrt=i
                return("square root is",sqrt)
