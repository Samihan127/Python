# //accept number and print number of digits
# //input: 7856
# //output:4


def iRet(iNo):
    iCnt=0
    while iNo!=0:
        iDig=iNo%10
        iCnt=iCnt+1
        iNo=iNo//10

    return iCnt

#main

if __name__=="__main__":
    iNo=int(input("enter a number:-"))
    iCnt=iRet(iNo)
    print(f"Number of digits are {iCnt}")