marks1=int(input("Enter the marks1:"))
marks2=int(input("Enter the marks2:"))
marks3=int(input("Enter the marks3:"))


total_percentage=((marks1 + marks2 + marks3)*100)/300
print(total_percentage)

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("congragulations you are passed")

elif(total_percentage==0):
    print("not a valid percentage")

else:
    print("you are failed",total_percentage )
