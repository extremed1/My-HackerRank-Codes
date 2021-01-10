#You are given a string  and width .
#Your task is to wrap the string into a paragraph of width .

#**this is without using textwrap**

import textwrap

def wrap(string, max_width):
    blocks = list((string[i:max_width+i] for i in range(0, len(string), max_width)))
    return "\n".join(blocks)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
