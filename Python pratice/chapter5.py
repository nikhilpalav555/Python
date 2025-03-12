# marks={
#     "nik":100,
#     "ravi" : 80,
#     "pramod":99

# }

# # print(marks, type(marks))
# # print(marks["nik"])

# print(marks, type(marks)) #prints the dict and gives what is the class type of marks
# print(marks["nik"]) #ptints the value of nik 
# print(marks["ravi"]) # prints value of ravi
# print(marks["nik"],marks["ravi"],marks["pramod"]) #prints the value of nik,ravi and promod we need to add , for each key pair function

# print(marks.items()) # prints key value pair in tuple format
# print(marks.keys()) # prints list of keys
# print(marks.values()) # prints list of values
# marks.update({"nik":120 , "paul":22}) #append the list using update function and also adds key value item in the list
# print(marks)
# c=marks.get("nik1") # this function acts same as print print(marks["nik"]) but if some value of key pair are not available it will returen none but using print function it will throw an error
# print(c)
# d=marks.pop("paul") #this functions pops the value from the dictionary
# print(d)



# a=[1,2,3,9,5,6,7,8]
# print(type(a))
# a.append(9)
# a.sort()
# print(a)





Team={
    "ROhit" : 100,
    "Kohli" : 80,
    "Hardik": 70,
    "Shreyas":65

}


print(Team, type(Team))
print(Team["ROhit"])
print(Team["Hardik"],Team["ROhit"])
print(Team.items())
print(Team.keys())
print(Team.values())
Team.update({"ROhit":264,"Kohli":180})
c=Team.get("ROhit1")
print(c)
d=Team.pop("ROhit")
print(d)