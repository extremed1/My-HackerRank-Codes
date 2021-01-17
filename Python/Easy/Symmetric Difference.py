#Given 2 sets of integers, M  and N , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

M, set1 = (input(),set(map(int,input().split())))
N, set2 = (input(), set(map(int,input().split())))

s = sorted(set1.symmetric_difference(set2))
for nums in s:
    print(nums)
