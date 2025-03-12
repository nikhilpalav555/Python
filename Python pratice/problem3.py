# #to detect spam message

# a= "buy now" 
# b="subscribe this"
# c="click this"
# d="you won"

# message=input("Enter the message:")

# if ((a in message) or (b in message) or (c in message) or (d in message)):
#     print("this is spam message")

# else:
#     print("this is not spam message")




#spam detector program

a="buy now"
b="Click here"
c="you won"

message=input("Enter the message:")

if ((a in message) or (b in message) or (c in message)):
    print("This is a spam email")

else:
    print("This is not a spam email")