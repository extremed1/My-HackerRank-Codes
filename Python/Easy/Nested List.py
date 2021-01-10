#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

from operator import itemgetter
students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        students.append([input(), float(input())])
        
mn = min(students, key = itemgetter(1))[1]
filtered = [i for i in students if i[1] != mn]
mn_filtered = min(filtered, key = itemgetter(1))[1]
remove = [i for i in filtered if i[1] == mn_filtered]
remove.sort()

for i in remove:
    print(i[0])
