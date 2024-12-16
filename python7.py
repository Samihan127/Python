
# //accept number and print  even digits
# //input: 234
# //output:2 4

# Function to accept a number and print even digits

def iRet(iNo):
    even_digits = []  # List to store even digits

    while iNo != 0:
        iDig = iNo % 10  # Get the last digit
        if iDig % 2 == 0:  # Check if the digit is even
            even_digits.append(str(iDig))  # Add to the list as a string
        iNo = iNo // 10  # Remove the last digit

    return " ".join(even_digits[::-1])  # Reverse the list and join with spaces



# Main function

if __name__ == "__main__":
    iNo = int(input("Enter a number: "))
    result = iRet(iNo)
    print(result)  # Print the even digits
