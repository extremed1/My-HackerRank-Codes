#You are given a string S .
#Your task is to print all possible combinations, up to size k , of the string in lexicographic sorted order.

from itertools import combinations
S, k = input().split()
string_sorted = sorted(S)


for i in range(1,int(k)+1):
    for j in combinations(string_sorted,i):
        print(''.join(j))
