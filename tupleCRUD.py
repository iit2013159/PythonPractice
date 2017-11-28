fsg = ('fjdgh','fdfgdgg' ,"gs") #Create tuple
print(fsg.index("gs"))

if fsg:
    fsg += ("abhishek","sameer")  #Update tuple

fsg = ()             #Remove tuple
if fsg:                     #Iterative Control statement
    fsg += ("abhishek","sameer")

else:
    fsg = ("have a test of list","search")
    fsg = fsg*2                     #multiple print
print(fsg)
print(tuple(reversed(fsg)))         #reverse the tuple when there is a single object then the reverse method will split all of them into char and then it is get being reversed
print(max(fsg))