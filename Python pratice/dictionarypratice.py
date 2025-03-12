newdict={
    "Raj" : 180,
    "Snehal" : 190,
    "Babita" : 140,
    "Jethalal" : 124
}

print(newdict)
print(type(newdict))
print(newdict["Raj"])
print(newdict.items())
print(newdict.keys())
print(newdict.values())
newdict.update({"Raj":160,"Priya":220})
print(newdict)
f=newdict.pop("Raj")
print(f)
newdict.get("Raj")
g=newdict.get("Raj1")
print(g)

