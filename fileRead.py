file = open("txt.txt",'a+')
file.write("Hey what do u do")
file.seek(6)
print(file.read())
file.close()