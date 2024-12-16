# Function to calculate the sum of numbers from 1 to n


def Sum(iVal):
    iSum = 0
    for i in range(1, iVal + 1):
        iSum += i
    return iSum

# Main 

if __name__ == "__main__":
    iNo = int(input("Enter a number: "))
    iRet = Sum(iNo)
    print(f"Sum is: {iRet}")
