# input: 7856
# output:
# 6
# 5
# 8
# 7

def iRet(iVal):
    while iVal!=0:
        iDigit=iVal%10
        print(iDigit)
        print()
        iVal=iVal//10
        

if __name__ == "__main__":
    iNo=int(input("enter a number:"))
    iRet(iNo)
