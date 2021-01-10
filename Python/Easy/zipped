#The National University conducts an examination of  students in  subjects.
#Your task is to compute the average scores of each student.

#The format for the general mark sheet is:
```
Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
'''


N,X = map(int,input().split())

subjects = []
for i in range(X):
    subjects.append(map(float, input().split()))
    
for scores in zip(*subjects):
    print(sum(scores)/len(scores))

