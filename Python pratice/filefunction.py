#reading multi lines in a  file

f = open ("weitefile.txt")

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# line3=f.readline()
# print(line3)

# line4=f.readline()
# print(line4)


# f.close()


line=f.readline()
while (line!=  ""):
    print(line)
    line=f.readline()

f.close()