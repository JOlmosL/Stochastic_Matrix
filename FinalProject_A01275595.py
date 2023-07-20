# Final Project: Stochastic matrices
# Jesus Olmos Larios - A01275595

import numpy as np
import random as rm
from numpy.linalg import matrix_power

def choices():
    print("\nWelocme to my Final Project\t-By A01275595-Jesus Olmos Larios")
    print("What do you want to do?")
    print("1 - Build your own Stochastic Matrix")
    print("2 - Auto-Generate Stochastic Matrix")
    print("3 - Exit")

def options():
    print("\nWhat do you want to do with it")
    print("1 - Calculate the probability from going to one state to another in n steps. ")
    print("2 - Calculate the long-term state (steady) of the matrix.")
    print("3 - Identify if the matrix is regular or not.")
    print("0 - Exit and Finish the program")

def checkStochastic(matrix, size):
    itIs = 1
    for i in range(0, size):
        Values = 0
        for j in range(0, size):
            Values = Values + matrix[i][j]
            #print(Values)
        if Values != 1:
            print("The created matrix is not a stochastic one =(\nReconstructing matrix...\n")
            itIs = 0
            return itIs
    print("---The created matrix is a stochastic one!!!---")
    itIs = 1
    return itIs

def probStates(matrix, elevate):
    a = np.round_(matrix, decimals=6)
    for i in range(0, elevate+1):
        print("Matrix in the", i, "state")
        print(np.round_(matrix_power(a, i), decimals=6),"\n")

def steadyState(matrix):
    obvious = 100
    steady = np.round_(matrix_power(matrix, obvious), decimals=6)
    compare = steady[1]
    if (steady == compare).all():
        print("\n---Steady State---\n", steady[1])
    else:
        print("\n---The generated matrix does not have a Steady State =(---\n")

def isRegular(matrix):
    result = np.all(matrix)
    if result:
        print("\n---The created matrix is Regular by default---\n", np.array(matrix), "\n")

    else:
        for i in range(2, 51):
          result2 = np.round_(matrix_power(matrix, i), decimals=6)
          result = np.all(result2)
          if result:
              print("\n---Matrix is Regular on its step", i,"---\n", result2, "\n")
              return 0
          else:
              pass
        print("\n---The created matrix is Non-Regular\n")



def main():
    loop = True
    while loop == True:
        choices()
        choice = float(input(">> "))

        if choice == 1:
            size = int(input("\nWhat will be the size of the Matrix?: "))
            loop2 = True
            while loop2 == True:
                matrix = []
                for i in range(0, size):
                    matrix.insert(i, [])
                    for j in range(0, size):
                        print("Value for position [", i+1,"][", j+1,"]")
                        number = float(input(">> "))
                        if number < 0:
                            print("Stochastic Matrices needs positive numbers!!!")
                            loop2 = False
                        value = round(number, 6)
                        matrix[i].insert(j, value)     

                print("\n---Generated Matrix:---")     
                print(np.array(matrix))

                loopbreaker = checkStochastic(matrix, size)
                #print(loopbreaker)
                if loopbreaker == 0:
                    loop2 = True
                
                elif loopbreaker == 1:
                    loop2 = False
                    loop3 = True
                    while loop3 == True:
                        options()
                        option = float(input(">> "))

                        if option == 1:
                            elevate = int(input("\nHow many steps would you like to include?: "))
                            probStates(matrix, elevate)

                        elif option == 2:
                            steadyState(matrix)
                            
                        elif option == 3:
                            isRegular(matrix)

                        elif option == 0:
                            print ("\nExiting ---Build your own Stochastic Matrix.exe---\n")
                            loop2 = False
                            loop3 = False


        elif choice == 2:
            print("\n---Automated 3x3 Stochastic Matrix---")
            decimals = 1000000
            matrix = []
            for i in range(3):
                list = []
                total = 0
                crtPrec = decimals
                for j in range(0, 3-1):
                    value = rm.randrange(crtPrec)
                    total += value
                    list.append(float(value)/decimals)
                    crtPrec -= value
                list.append(float(decimals - total)/decimals)
                matrix.append(list)
            print(np.array(matrix))

            loop2 = True
            while loop2 == True:
                options()
                option = float(input(">> "))

                if option == 1:
                    elevate = int(input("\nHow many steps would you like to include?: "))
                    probStates(matrix, elevate)

                elif option == 2:
                    steadyState(matrix)
                            
                elif option == 3:
                    isRegular(matrix)

                elif option == 0:
                    print ("\nExiting ---Auto-Generate Stochastic Matrix.exe---\n")
                    loop2 = False



        elif choice == 3:
            print("\nGood Bye =D")
            loop = False

        else:
            print("Invalid Input. Please try again\n")

main()