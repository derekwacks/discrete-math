# Python program that prints prime numbers up to a user specified integer 
# user input n
size = input("Enter n: ")
sizeInt = int(size)
#creates list of ints of size n
listOfInts = [i for i in range(2,sizeInt+1)]

#print(listOfInts)

for i in listOfInts:
    #print(i)
    z = sizeInt//i
    #print(z)

    #print(i, " has ", z, " multiples in the list")
    """
    for j in listOfInts:
        for k in range(2,z+1):
            listOfInts.remove(k*j)
            """
    if z>1:
        for k in range(2,z+1):
            #print("the ",k, " time")
            #print("removing multiples of ", i)
            if k*i in listOfInts:
                listOfInts.remove(k*i)     
  
print("New List of primes up to n")
print(listOfInts)
