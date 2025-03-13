#create a txt file

a= '''Wow its a good day
hello this is a file type
we will read this file line by line
we will get to know file function
we will learn lot about it '''

f=open("weitefile.txt","w")
f.write(a)
print(f)
f.close()