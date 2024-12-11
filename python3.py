#program implementing menu driven application for computing all Arithmetic Operations by using match  ... case


print("===================================================")
print("\tA r i t h m e t i c  O p e r a t i o n s")
print("===================================================")
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Floor Division")
print("\t6.Modulo Division")
print("\t7.Exponentiation")
print("\t8.Exit")
print("===================================================")
ch=int(input("Enter Ur Choice:"))
match(ch):
	case 1:
		n1=(input("Enter First Value for Addition:"))
		n2=(input("Enter Second Value for Addition:"))
		print("sum({},{})={}".format(n1,n2,n1+n2))
	case 2:
		print("Enter Two values for substraction:")
		n1,n2=float(input()), float(input())
		print("sub({},{})={}".format(n1,n2,n1-n2))
	case 3:
		print("Enter Two values for Multiplication:")
		n1,n2=float(input()), float(input())
		print("mul({},{})={}".format(n1,n2,n1*n2))
	case 4:
		print("Enter Two values for Division:")
		n1,n2=float(input()), float(input())
		print("Div({},{})={}".format(n1,n2,n1/n2))
	case 5:
		print("Enter Two values for Floor Div:")
		n1,n2=float(input()), float(input())
		print("Floor Div({},{})={}".format(n1,n2,n1//n2))
	case 6:
		print("Enter Two values for Modulo Divisioin:")
		n1,n2=float(input()), float(input())
		print("Mod({},{})={}".format(n1,n2,n1%n2))
	case 7:
		print("Enter Two values for Exponentiation:")
		n1,n2=float(input()), float(input())
		print("pow({},{})={}".format(n1,n2,n1**n2))
	case 8:
		print("\nThanks for using this calculator")
		exit() # pre-defined function used to terminate the program physically.
	case _:
		print("Ur Selection of Operation is wrong!--execute again")
