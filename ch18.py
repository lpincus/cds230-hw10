# Python Data and Computations in the book, Computational Methods for Bioinformatics: Python 3.4, Third Edition by Jason Kinser.
import numpy as np

np.random.seed(10)
# 1. Compute the average of sets of random numbers. 
# The number of samples in the sets should be 
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 and 4096. 
# Plot the average of the random values in each set 
# versus the number of samples. 
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



# 3. Compute the average of 10,000 samples of √ x where x represents random numbers. Is the result the same as √ 0.5? 
# 4. Plot the histogram of 10,000 samples from a normal distribution with µ = 0.5 and σ = 0.3. 
# 5. Plot the histograms of two normal distributions. The first has 10,000 samples with µ = 0.5 and σ = 0.4. The second has 9,000 samples with µ = 0.3 and σ = 0.2. What is the value of x where the two distributions cross over? 
# 6. Create a random DNA string with 1000 letters, but the probability of having an ’A’ is twice as much as the other three letters. 
# 7. Create a random amino acid string with 1000 letters.
