from collections import Counter
import math
a= input("Enter Boy Name: ")
b= input("Enter Girl Name: ")

def cal_words(name):
    counts=dict()
    for i in name:
        try:
            counts[i]= counts[i]+1
        except KeyError:
            counts[i] =1
    return counts

c=cal_words(a)
d=cal_words(b)
for key in set(c) | set(d):
    get_a = c.get(key,0)
    get_b = d.get(key,0)
    if((get_a and get_b > 0)):
        get_same_val= min(get_a,get_b)
        a = a.replace(key, "", get_same_val)
        b = b.replace(key, "", get_same_val)
remaining_count=len(a+b)

def flames(remaining_count):
    c = 0
    a = {'F': True, 'L': True, 'A': True, 'M': True, 'E': True, 'S': True}
    b = remaining_count

    while sum(a.values()) > 1: 
        for i in a: 
            if a[i]:
                c += 1
                if c == b:
                    a[i] = False
                    c = 0 
                    
    for key, value in a.items():
        if value:
            return key

print("Final Letter:",flames(remaining_count))

    
    


