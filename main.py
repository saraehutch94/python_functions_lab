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

# Exercise 3:

def occurances(string1, string2):
  second_string_length = len(string2)
  count = 0

  for index, letter in enumerate(string1):
    if(string1[index:index+second_string_length]) == string2:
      count += 1

  return count

print(f'Exercise 3: {occurances("fleep floop", "fl")}')

# Exercise 4:

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(f'Exercose 4: {product(4, 0.5, 5)}')