# Python Data and Computations in the book, 
# Computational Methods for Bioinformatics: Python 3.4, 
# Third Edition by Jason Kinser.

import numpy as np
import math 

np.random.seed(10)
# 1. Compute the average of sets of random numbers. 
# The number of samples in the sets should be 
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 and 4096. 
# Plot the average of the random values in each set 
# versus the number of samples. 
def prob1():
    samplenumbers=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    averages=[]
    for n in samplenumbers:
        rand_num = np.random.rand(n).mean()
        averages.append(rand_num)
        print("{}, \t {}".format(n, rand_num))
    print(samplenumbers)
    print(averages)


# 2. Compute the average of 10,000 samples 
# of x^2 where x represents random numbers. 
def prob2():
    rands=np.random.rand(10000)
    randsqr=[]
    for i in rands:
        randsqr.append(i*i)
    avg=np.array(randsqr).mean()
    print(avg)
# prob2()

# 3. Compute the average of 10,000 samples of √ x 
# where x represents random numbers. 
# Is the result the same as √ 0.5? 
def prob3():
    rands=np.random.rand(10000)
    randsqr=[]
    for i in rands:
        randsqr.append(math.sqrt(i))
    avg=np.array(randsqr).mean()
    print(avg)  
    print(math.sqrt(0.5))
# prob3()

# 4. Plot the histogram of 10,000 samples 
# from a normal distribution 
# with µ = 0.5 and σ = 0.3. 
def prob4():
    rands=np.random.normal(0.5, 0.3, 10000)
    y, x = np.histogram(rands)
    print(x)
    print(y)
# prob4()


# 5. Plot the histograms of two normal distributions. 
# The first has 10,000 samples 
# with µ = 0.5 and σ = 0.4. 
# The second has 9,000 samples 
# with µ = 0.3 and σ = 0.2. 
# What is the value of x where the two distributions cross over? 

def prob5():
    rands=np.random.normal(0.5, 0.4, 10000)
    y, x = np.histogram(rands)
    print(x)
    print(y)
    rands=np.random.normal(0.3, 0.2, 9000)
    y, x = np.histogram(rands)
    print(x)
    print(y)
# prob5()


# 6. Create a random DNA string with 1000 letters, 
# but the probability of having an ’A’ is twice as much as the other three letters. 
def prob6():
    dna = "A A T C G".split()
    dnastring = "".join(np.random.choice(dna, 1000))
    print(dnastring)
# prob6()

# 7. Create a random amino acid string with 1000 letters.
def prob7():
    aas="A R N D B C E Q Z G H I L K M F P S T W Y V".split()
    proteinstring="".join(np.random.choice(aas, 1000))
    print(proteinstring)
# prob7()