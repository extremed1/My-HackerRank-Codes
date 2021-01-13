#You have a non-empty set s, and you have to execute N commands given in N  lines.
#The commands will be pop, remove and discard.


n = int(input())
s = set(map(int, input().split()))
N = int(input())


for i in range(N):
    func,*nums = input().split() 
    getattr(s,func)(*(int(num)for num in nums))
print(sum(s))
