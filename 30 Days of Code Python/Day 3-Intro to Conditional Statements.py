#Given an integer,N , perform the following conditional actions:

#If N is odd, print Weird
#If N is even and in the inclusive range of 2  to 5, print Not Weird
#If N is even and in the inclusive range of 6 to 20, print Weird
#If N is even and greater than 20 , print Not Weird
#Complete the stub code provided in your editor to print whether or not  is weird.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())


    
if N % 2 != 0:
    print("Weird")
elif N % 2 == 0:
     if N in range(2,6) or N > 20:
        print("Not Weird")
     else:
        print("Weird")
