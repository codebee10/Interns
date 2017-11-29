msg = input("Enter string: ")
count=0
for i in msg:
	if(i.isupper()):
	  count=count+1
print("Count: ",count)