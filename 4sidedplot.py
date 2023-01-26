 
import sys
import numpy as np
import matplotlib.pyplot as plt

#takes a .txt file, reads it, and makes a list

filename=input("input .txt file: ")

with open(filename, "r") as f:
    myArray = f.read().split()

for i in range(0, len(myArray)):
    myArray[i] = int(myArray[i])

#makes plot of numbers from my array

n, bins, patches = plt.hist(myArray, 4, density=True, facecolor='r', alpha=0.75)

plt.xlabel('Random #s')
plt.ylabel('Probability')
plt.title('Random Numbers')
plt.grid(True)

plt.show()
