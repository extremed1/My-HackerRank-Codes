#Apply your knowledge of the .add() operation to help your friend Rupal.

#Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

#Find the total number of distinct country stamps.

stamps = set()

for i in range(int(input())):
    stamps.add(input())
print(len(stamps))
