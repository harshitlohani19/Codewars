'''
The number 
89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 

The next number in having this property is 135 135:
See this property again: 
135
Task [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range 
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!
'''
#
def sum_dig_pow(a, b):
    eureka_numbers = []
    for num in range(a, b + 1):
        sum_dig_pow = 0
        digits = str(num)
        for i in range(len(digits)):
            sum_dig_pow += int(digits[i]) ** (i + 1)
        if sum_dig_pow == num:
            eureka_numbers.append(num)
    return eureka_numbers