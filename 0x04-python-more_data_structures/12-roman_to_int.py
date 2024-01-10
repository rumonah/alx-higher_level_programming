#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string)!=str:
        return 0
    data = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    numbers =[data[x] for x in roman_string] + [0]
    rep = 0
    for r in range(len(numbers)-1):
        if numbers[r]>=numbers[r+1]:
            rep += numbers[r]
        else:
            rep -= numbers[r]
            return rep
