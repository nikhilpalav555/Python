# #program for multiplication of a number
# a=int(input("enter the no:"))

# for i in range(1,11):
#     print(f"{a} X {i}={a*i}")



#program to print persons name starts with s in given list

# l=["Nikhil","Sanika","Soham","Shizuka"]


# for name in l:
#     if (name.startswith("S")):
#         print(f"{name} you are invited")


# #program for multiplication of a number using while loop


# a=int(input("enter the no:"))

# i=1

# while (i<=11):
#     print(f"{a} X {i}={a*i}")
#     i+=1



#program to find given no is prime or not

# a=int(input("enter the no:"))
# for i in range(1,a):
#     if(a%i)==0:
#         print("number is a even no")
#         break




# a=int(input("enter the no:"))

# for i in range (2,a):
#     if(a%i)==0:
#         print("This is not a prime number")
#         break
# else:
#     print("This is a prime no.")












# a=int(input("Enter the number:"))
# for i in range (2,a):
#     if(i%2)==0:
#         print("This is even no")
#         break
# else:
#     print("This is an odd no.")  






# a=int(input("Enter the no.:"))

# i=1

# while (i==a):
#     print(f"factorial of a given no= {a*i}")
#     i+=1


# a=int(input("Enter the given no:"))

# i=1

# while (i<=a):
#     i=a*i
# print(i)

# n=int(input("Enter the number n:"))

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")



# n=int(input("Enter the given no."))

# for i in range(1,n+1):
#     print(" "*(n+1),end="")
#     print("*"*i,end="")
#     print("")


# n=int(input("Enter the given no."))
# for i in range(1,n+1):
#     if(i==1  or  i==n):
#         print("*"*n,end="")

#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

#program  to print multiplication of no. inn reverse  order 
# n=int(input("Enter the given no."))
# for i in range(1,11):
#     print(f"{n}X{11-i}={n*(11-i)}") 

# #function defination
# def avg():

#     a=int(input("Enter the given no:"))
#     b=int(input("Enter the given no:"))
#     c=int(input("Enter the given no:"))

#     average=(a+b+c)/3

#     print(average)
# #function call
# avg()


# i=3
# avg()
# while (i==avg):
#     if i==avg():
#         print(f"Okay we met our condition, {avg}")

#     else:
#         print(f"Okay our condition is not met, {avg}")



#dfunction with argumets

# def goodday(name,ending):
#     print("Goodday",name)
#     print(ending)
#     return "Okay"

# a=goodday("Nikhil","THanks")



# #default functuion
# def goodday(name,ending="Bye"):
#     print(f"Goodday,{name}")
#     print(ending)


# goodday("Harry","Get out")
# goodday("Nikhil")


#program to print factorial of no. using recursion
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter the no:"))
print(f"factorial of given no. is {factorial(n)}")