# Exercise 1:

def sum_to(n):
  sum = 0
  for num in range(0, n + 1):
   sum += num
  return sum

print(f'Exercise 1: {sum_to(6)}')

# Exercise 2:

def largest(list):
    largestNumber = 0
    for num in list:
      if(num > largestNumber):
        largestNumber = num
    return largestNumber

print(f'Exercise 2: {largest([10, 4, 2, 231, 91, 54])}')

