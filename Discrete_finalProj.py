import time
import matplotlib.pyplot as plt
import math
import numpy as np
 
againBool = True
while againBool == True:
    #import arrays
    print("What would you like to do?")
    print()
    possible = [1, 2, 3]
    okay = False
    while okay == False :
        menuChoice = int(input("You may:\nRun the GCD code (enter 1)\nList the primes up to an integer of your choice (enter 2)\nFind all primes up to a few large hardcoded N's and see the runtimes (enter 3) "))                     
        if menuChoice in possible:
            okay = True
        else: 
            print()
            print("Please choose option 1, 2, or 3")

    #_______________________________________________
    # Problem 1: GCD
    # Written by Matthew Roman (smr2219)
    if menuChoice == 1:
        #Problem 1
        def gcd(a, b):
          if a<=0 or b<=0:
            raise Exception("Please ensure that inputs are greater than 0.")
          r = a%b 
          print ("Modulus calculation: " + str(a%b))
          print ("Does a%b equal zero? " + str(r==0))
          if r==0:
            print ("Then b is our GCD!")
            return b 
          else:
            print ("Time to recurse! Now, a = "+str(b)+", and b = "+str(r))
            return gcd(b,r)

        #Test cases
        print(gcd(4278,8602))
        print("")
        print(gcd(406,555))
        print("")
        print(gcd(244,354))
        print("")
        print(gcd(3000,9000))
        print("")
        print(gcd(40000,123456))
        print("")
        print(gcd(12345678,12345678910))
        print("")
        print(gcd(89345892349,10924983985))
        print("")
        print(gcd(7895232,63161856))       
    #_______________________________________________
    # Code that prints all primes up to a user specified integer 
    
    if menuChoice == 2:
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

    if menuChoice == 3:

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

    okayAgainChoice = False
    while okayAgainChoice == False:
        againChoice = str(input("Would you like to choose again? (y/n) "))  
        if againChoice == 'y':
            print("Cool! ")
            print()
            againBool = True
            okayAgainChoice = True
        if againChoice == 'n':
            print("Goodbye world. ")
            againBool = False
            okayAgainChoice = True


