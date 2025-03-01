# Exercise 36: Designing and Debugging

import sys

F = int(input("Enter temp in Fahrenheit:"))

C = ( F - 32) / 1.8
print(C)

print(f'%.2f\N{DEGREE SIGN} Fahrenheit =  %.2f\N{DEGREE SIGN} Celsius'
      % (F ,C))

print('%.1f\N{DEGREE SIGN}F to %.1f\N{DEGREE SIGN}C'
      % (F, C))