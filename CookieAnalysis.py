# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from sorting.MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)

    quartiles = [25, 50, 75, 90]
    quarperc = ['25%','50%','75%','90%']
    quarlocate = np.percentile(times, quartiles)

    #prints out the values of the quartiles
    print(quarlocate)

     # creates a histogram of our sorted data with red lines displaying the quantiles 
    n, bins, patches = plt.hist(times, 100, density=True, facecolor='green', edgecolor= 'black', alpha=0.75)
    
    plt.xlabel('Random #s')
    plt.ylabel('Probability')
    plt.title('Random Numbers')
    plt.grid(True)

    #labels for the quartiles
    plt.text(quarlocate[0],0.80, quarperc[0], color='black')
    plt.text(quarlocate[1],0.70, quarperc[1], color='black')
    plt.text(quarlocate[2],0.60, quarperc[2], color='black')
    plt.text(quarlocate[3],0.50, quarperc[3], color='black')
    
    #quartile lines
    for q in quarlocate:
        plt.axvline(q ,color='red')
        plt.text(q, -.10, round(q, 2), color='black', rotation= 90)
            

    plt.show()

