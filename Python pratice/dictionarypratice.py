# newdict={
#     "Raj" : 180,
#     "Snehal" : 190,
#     "Babita" : 140,
#     "Jethalal" : 124
# }

# print(newdict)
# print(type(newdict))
# print(newdict["Raj"])
# print(newdict.items())
# print(newdict.keys())
# print(newdict.values())
# newdict.update({"Raj":160,"Priya":220})
# print(newdict)
# f=newdict.pop("Raj")
# print(f)
# newdict.get("Raj")
# g=newdict.get("Raj1")
# print(g)




# dict={
#     "name":"Nikhil",
#     "Age":25,
#     "Status":"Single"
# }


# print(dict["Status"])

# dict.update({"surname":"palav"})
# print(dict)
# # dict.clear()
# # print(dict)
# dict.items()
# print(dict)
# print(dict.keys())
# # print(dict)


my_vehicle={
    "modle":"Ford",
    "make":"Explorer",
    "year":2018,
    "milage":4000

}


# # for i in my_vehicle:
# #     print(my_vehicle)

# my_vehicle.update({"vehicle2":{
#                        "modle":"Ford",
#                         "make":"Explorer",
#                         "year":2018,
#                         "milage":4000}
#                    })

# print(my_vehicle)

# my_vehicle.update({"Vehicle2":{
#                   "no_of_tires":4}})

# print(my_vehicle)

# my_vehicle.popitem({"Vehicle2":{"milage"}})

# print(my_vehicle)


for x,y in my_vehicle.items():
    print(x,y)


vehicle2=my_vehicle.copy()

vehicle2.update({"no_of_tires":4})

vehicle2.pop("milage")

for i in vehicle2:
    print(i)

print(vehicle2)


