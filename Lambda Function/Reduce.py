from functools import reduce

li=[2,12,34,5]
sum1=(reduce(lambda a,b:a if a>b else b,li))
print(sum1)



li=[2,3,4,5,6,7]
sum=reduce((lambda x,y:x+y),li)
print(sum)
