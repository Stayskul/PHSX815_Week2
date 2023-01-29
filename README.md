# PHSX815_Week2
Contains the homework assignments for week 2

Instructions for HW 3
Homework 3 was adapted from files from https://github.com/crogan/PHSX815_Week2/tree/master/python as well as from my own week 1 repository

First generate a set of random dice (D4) rolls using 4sided.py and have it write the output to a .txt file
    I used "python3 4sided.py -Ntoss 10 -Ntoss 10 > Rando.txt
    This will create a file called Rando.txt which has all of our dice rolling
    
Next use the 4sidedplot.py code to make a histrogram from our .txt file
Simply run 4sidedplot.py, it will ask you to input a .txt file... type in the name of the file you created with 4sided.py... in my case, Rando.txt
Then, it will created a histrogram showing the frequencies of each number 1-4 in our set of dice rolls.

additional note: in the 4sided.py file you will have the change the location of the Random.py file, so that the code finds in it properly.


Intructions for HW 4
Homework 4 was adapted from  https://github.com/crogan/PHSX815_Week2/tree/master/python as well as from my own week 1 repository
I also used some reference code for creating the quartiles https://stackoverflow.com/questions/43360414/annotate-the-quartiles-with-matplotlib-in-a-normal-distribution-plot

First in both CookieTimer.py and CookieAnalysis.py, you will need to change the locations of the Random.py and the MySort.py files, so that the code can find it.
Once you do this, run the CookieTimer.py file and have it output the result to a .txt file. Something like "python3 CookieTimer.py -Nmeas 1000 > numbers.txt".
Once you have the .txt file, run CookieAnalysis.py (inputting the .txt file)(and using the sorting  method of your choice). 
Something like "python3 CookieAnalysis.py numbers.txt".
The final result will be a printing of 4 quartile locations, and a beautiful histogram of my sorted data (the figure I generated is included in this repository).
