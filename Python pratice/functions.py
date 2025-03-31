# name="   nikhil     palav       "
# print(len(name)) #returns length of string
# print(name.upper()) #converts string to upper case
# print(name.lower()) #converts string to lower case
# print(name.strip()) #removes whitespace from sring
# print(name.lstrip()) #removes whitespace from  left hand side from string
# # print(name.rstrip())#removes whitespace from  right hand side from string
# # print(name.replace("palav", "Hemant"))  # replaces the string to another string 

# #pratice set
# name = "nikhilpalav"
# s='this','is','hellow','world','program'
# newname="This","is","simple"
# print(name.strip())
# print(name.lstrip())
# print(name.strip())
# print(len(name))
# print(name.replace("palav","Hemant"))
# print(name.upper())
# print(name.lower())
# print(name[0:1])
# print(name[1])
# print(name[2:5])
# # a=int(input("Enter number a is:"))
# # b=int(input("Enter number b is:"))
# # c=a+b
# # print(c)
# print("".join(newname))
# print("".join(s)) #this program joins the string and removes empty spaces within them
# print(newname.index("This")) #this program gives the index of a string in group of strings
# print(newname.count("i")) #this program gives occurance of a substrin characters only in a continous string 
# print(name.endswith("av")) # gives boolean value and justifies the statement as true or false
# print(name.startswith("ni")) # gives boolean value and justifies the statement as true or false
# print(name.capitalize()) # capatalizes starting letter of string    

def data(firstame,lastname,age):
    dictory={"firstame":firstame,
                 "lastname":lastname,
                 "age":age}
    return dictory


newdata=data(firstame="nikhil",lastname="palav",age=25)
print(newdata)



