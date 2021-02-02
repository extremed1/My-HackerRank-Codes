#You are given a string S.
#Your task is to find out whether S is a valid regex or not.

import re

for i in range(int(input())):
    answer = True
    try:
       is_valid = re.compile(input())
    except re.error:
        answer = False
    print(answer)
