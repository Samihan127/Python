#print [1,4,9,16,25,36,49,64,81,100]

num=int(input("enter a number:"))
for i in range(1,num+1):
    print(i*i)

#WAP to find sum of first n numbers 

num1=int(input("enter a number:"))
i=1
sum=0
while(i<=num1):
    sum+=i
    i+=1
print("sum is",sum)
