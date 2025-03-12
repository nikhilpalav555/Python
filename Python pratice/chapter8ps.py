# #program to print greatest of 3 no. using function
# def greatest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a=int(input("Enter number a:"))
# b=int(input("Enter number b:"))
# c=int(input("Enter number c:"))


# print(greatest(a,b,c))

# #print degree to celcius
# def t_c():
#     c=(t - 32)*5/9
#     return c


# t=int(input("Enter the temperature:"))
# print(t_c())


# #program to skip new line in a program we can use end function
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")



# #program to print sum of n natural no.
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# # a=int(input("Enter the no.:"))
# print(sum(5))

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(3)


# #program to ptiny inch to cm
# def inchtocm(inch):
#     return inch * 2.54

# n=int(input("ENter the value in inch:"))
# print(f"{inchtocm(n)}")


# #program to remove items from list and to append items in list
# l=["nikhil","Sahil", "Akhil","Sunil","il"]

# def remove(l,words):
#     n=[]
#     for item in l:
#         if not(item==words):
#             n.append(item.strip(words))
#     return n



# print(remove(l,"il"))




#python function to print multiplication of given no.
def multiply(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
    

n=int(input("Enter the given no.:"))
print(multiply(n))
