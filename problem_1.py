# problem 1
print "Euler Problem 1"

sum = 0

for number in range (1, 100):
  if not (number % 3 and number % 5):
    print number , " "
    sum += number

print "\nsum is ", sum
