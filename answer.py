fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
 
   new=line.rstrip().split()
   for element in new:
       if element in lst:
           continue 
       else:
            lst.append(element )
lst.sort()
print (lst)

