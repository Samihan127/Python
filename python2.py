# Function to calculate the sum of numbers from 1 to n

def Sum(iVal):
    iSum = 0
    for iCnt in range(1, iVal + 1):
        iSum += iCnt
    return iSum

# Main 

if __name__ == "__main__":
    iNo = int(input("Enter a number: "))
    iRet = Sum(iNo)
    print(f"Sum is: {iRet}")
