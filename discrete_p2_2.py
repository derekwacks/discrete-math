import time
import matplotlib.pyplot as plt
import math
import numpy as np

# user input n
#size = input("Enter n ")
#nList = [10000]
nList = [10,100,1000,10000,20000,30000]
nListnp = np.array(nList)
timeList = []
#normalizedTimeList = []
#list = [10,100,1000,10000,100000,1000000]

for i in nList:
    sizeInt = i
    #creates list of ints of size n
    start = time.time()
    listOfInts = [i for i in range(2,sizeInt+1)] #list of all ints up to n 
    #print(listOfInts)
    for j in listOfInts:
        #print(i)
        z = sizeInt//j
       # print(z)

        #print(i, " has ", z, " multiples in the list")
        #print()
        """
        for j in listOfInts:
            for k in range(2,z+1):
                listOfInts.remove(k*j)
                """
        if z>1:
            for k in range(2,z+1):
             #   print("removing multiples of ", i)
                if (k*j) in listOfInts:
                    listOfInts.remove(k*j) # All remaining elements in listOfInts are prime    
        
    #print("New List of primes up to n")
    #print(listOfInts)
    end = time.time()
    #x = math.log(end-start)
    timeList.append(end-start)
    #print(listOfInts)
    #print("THERE ARE ", len(listOfInts), " PRIMES IN THE FIRST ", i, " NUMBERS")
    #print()
    #timeList.append(x)
    print(end-start)

#maxVal = max(timeList)
#for i in timeList:
#    normalizedTimeList.append(i/maxVal)
#plt.plot(nList,normalizedTimeList)
x = np.array(timeList)

plt.plot(nListnp, x)
plt.xlabel('N')
plt.ylabel('Time')
plt.show()

