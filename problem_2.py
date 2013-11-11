# problem 1

def fibonacci(num):
  if (num <= 2):
    return 1

  if num in fib_cache:
    return fib_cache[num]
   
  fib_cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
  return fib_cache[num]

print "Euler Problem 2"

fib_cache = {}

print fibonacci(33) # 3524578 

even_fib_sum = 0

for key in fib_cache:
  if not (fib_cache[key] % 2):
    even_fib_sum += fib_cache[key]

print "sum of even numbers under 4 million in fibonacci sequence:", even_fib_sum
