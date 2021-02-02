#The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.
#You are given two values a and b.
Perform integer division and print a/b.

for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
        
