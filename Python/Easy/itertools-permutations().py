#You are given a string S .
#Your task is to print all possible permutations of size S of the string in lexicographic sorted order k.

from itertools import permutations

S,k = input().split(' ')
for i in list(permutations(sorted(S), int(k))): 
    print(''.join(i))
