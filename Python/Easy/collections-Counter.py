# Raghu is a shoe shop owner. His shop has X number of shoes.
#He has a list containing the size of each shoe he has in his shop.
#There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

#Your task is to compute how much money Raghu  earned

from collections import Counter


def total_amount(shoe_list, customer_size_price_list):
    l = []
    counts = Counter(shoe_list)
    for inner_list in customer_size_price_list: #iterating through nested list
        if inner_list[0] in counts.keys(): #checking if 1st element of smaller list is is a dictionary key
            if counts[inner_list[0]] > 0: # Checking if key value is > than 0
                l.append(inner_list[1]) #if key value greater than 0, append 2nd item of smaller list to l
                counts[inner_list[0]] -= 1 # decrease key value by 1 
            else:
                counts[inner_list[0]] == 0 #preventing key values from going below 0
        else:
            continue
    return sum(l)
    
X = int(input()) #number of shoes in store
sizes = map(int,input().split()))
N = int(input()) #number of customers

d = list(map(int,input().split())) for i in range(N)])

total_amount(sizes,d)

