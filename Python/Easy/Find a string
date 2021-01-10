#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

#NOTE: String letters are case-sensitive.





def count_substring(string, sub_string):
    count = 0 
    position = 0
    
    while True:
        position = string.find(sub_string, position)
        if position > -1:
            count += 1
            position += 1
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
