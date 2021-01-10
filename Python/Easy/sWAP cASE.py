#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    chars = list(s)
    swaps = []
    for i in chars:
        if i.isupper() == True:
            swaps.append(i.lower())
        else:
            swaps.append(i.upper())
    return "".join(swaps)
          
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
