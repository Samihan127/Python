# //accept number and print sum of even digits
# //input: 234
# //output:6


def iRet(iNo):
    Even_Sum=0

    while iNo!=0:
        iDig=iNo%10
        if(iDig%2==0):
            Even_Sum=Even_Sum+iDig
        iNo=iNo//10

    return Even_Sum

#Main

if __name__=="__main__":
    iNo=int(input("enter a number:"))
    print(iRet(iNo))