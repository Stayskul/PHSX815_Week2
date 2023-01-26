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
