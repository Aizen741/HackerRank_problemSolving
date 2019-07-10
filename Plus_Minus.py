from decimal import *

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#Number of positives
num1 = 0
#Number of negatives
num2 = 0
#Num of zeros
num3 = 0

for integer in arr:
    if (integer > 0):
        num1 = num1 + 1

    elif (integer < 0):
        num2 = num2 + 1

    else:
        num3 = num3 + 1

fraction_Positive_value = Decimal(num1) / Decimal(n)
# Precision of positive value
Precision1 = format(fraction_Positive_value, '.6f')
print(fraction_Positive_value)

fraction_Negative_value = Decimal(num2) / Decimal(n)
#Precision of negative value
Precision2 = format(fraction_Negative_value, '.6f')
print(fraction_Negative_value)

fraction_Zeros_values = Decimal(num3) / Decimal(n)
#Precision of zero value
Precision3 = format(fraction_Zeros_values, '.6f')
print(fraction_Zeros_values)


