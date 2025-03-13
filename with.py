#using with statement without using close 

with open("weitefile.txt") as f:
    print (f.read())