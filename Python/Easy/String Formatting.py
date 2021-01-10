#Given an integer,n, print the following values for each integer i from 1 to i :

#1.Decimal
#2.Octal
#3.Hexadecimal (capitalized)
#4.Binary
#The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .




def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f'{dec} {octal} {hexa} {binary}')
        
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
