# Define the requried function addition().
# Input the values of a and b respectively.
def addition(a, b):
  # The base or stopping case: when a is zero
  if a == 0:
    # Return a+b, i.e. 0+b.
    return b
  # The recursive process: when a is greater than zero
  else:
    # Each time, one is substracted from a and add one to the addition of a and b.
    return addition(a - 1, b) + 1

# Example:
a = 5
b = 6
print(addition(a, b))
# 11

""""""

# Define the requried function average().
# Input the array A, the sum of the array (default: 0), and the number of calculation (default: 1).
def average(A, sum=0, num=1):
  # The base or stopping case: when there is only one element in A.
  if len(A) == 1:
    # Return the sum of the last element of A and the sum of the remaining elements over the number of calculation.
    return (sum + A[0]) / num
  # The recursive process: when there are more than one elements in A.
  else:
    # Each time, the first element of A is exctracted and added to the sum and the number of calculation increases by one.
    return average(A[1:], sum + A[0], num + 1)

# Example:
A = [3, 4, 5, 6, 7]
print(average(A))
# 5.0

""""""

# Define the requried function gcd().
# Input two numbers: x and y.
def gcd(x, y):
  # The base or stopping case: when y is smllar than or equal to x and the remainder of x upon division by y is zero.
  if y <= x and x % y == 0:
    # Return y directly.
    return y
  # The first recursive step: when x is smaller than y, though this could happen at most only once.
  elif x < y:
    # Switch the position of x and y to make sure y is smaller than or equal to x.
    return gcd(y, x)
  # The second recursive process: when the condition is not either of the above two conditions.
  else:
    # Each time, compute the remainder of x upon division by y. Also, the remainder is always smaller than the divisor.
    return gcd(y, x % y)

# Examples:

x = 8
y = 4
print(gcd(x, y))
# 4

x = 4
y = 8
print(gcd(x, y))
# 4

x = 13
y = 5
print(gcd(x, y))
# 1

""""""

# Define the requried function gfib().
# Input the initial two numbers: f0 and f1, and the target number: n.
def gfib(f0, f1, n):
  # The base or stopping cases: when n is f0 and when n is f1.
  if n == 0:
    # Return f0 or f1 directly.
    return f0
  elif n == 1:
    return f1
  # The recursive process: when n is not f0 or f1.
  else:
    # Each time, f(n) is converted into f(n-1) and f(n-2).
    return gfib(f0, f1, n-1) + gfib(f0, f1, n-2)

# Examples:

f0 = 0
f1 = 1
n = 10
print(gfib(f0, f1, n))
# 55

f0 = 2
f1 = 3
n = 10
print(gfib(f0, f1, n))
# 233

f0 = 8
f1 = 3
n = 10
print(gfib(f0, f1, n))
# 437

""""""

# The recursive version
def rec(n):
  if f(n) == False:
    return rec(g(n))
  else:
    return 0

# The iterative version
def rec(n):
  m = n
  while f(m) == False:
    m = g(m)
  return 0

""""""

# The iterative version
def compare_pair(A):
  # Use an auxiliary variable to save the maximum value found.
  value = A[0]
  # Search from the beginning to the end.
  for element in A:
    # If the checked element is greater than the auxillary variable, assign it to the auxillary variable.
    if element > value:
      value = element
  return value

A = [3, 4, 6, 2, 9, 7]
print(compare_pair(A))
# 9

# The recursive version
def compare_pair(A):
  # The base or stopping case: when there is only one or no element left.
  if len(A) <= 1:
    return A[0]
  # The recursive case: when there are more than one element, i.e. at least two elements in A.
  else:
    # Compare the first and the second element.
    if A[0] < A[1]:
      # If the first element is smaller, remove the first element.
      return compare_pair(A[1:])
    else:
      # If the second element is smaller, remove the second element.
      return compare_pair([A[0]] + A[2:])
    
A = [3, 4, 6, 2, 9, 7]
print(compare_pair(A))
# 9

""""""

# The iterative version
def sorting(A):
    # The base or stopping case: when there is only one or no element left.
    if len(A) <= 1:
        return A
    # The recursive case: when there are more than one element, i.e. at least two elements in A.
    else:
        # Set A[0] as the mid-point.
        # Formulate a sub-array before A[0], i.e. the elements smaller than A[0].
        before_sub = []
        for element in A[1:]:
          if element <= A[0]:
            before_sub.append(element)
        before_sub = sorting(before_sub)
        # Formulate a sub-array after A[0], i.e. the elements smaller than A[0].
        after_sub = []
        for element in A[1:]:
          if element > A[0]:
            after_sub.append(element)
        after_sub = sorting(after_sub)
        return before_sub + [A[0]] + after_sub

A = [3, 4, 6, 2, 9, 7]
print(sorting(A))
# [2, 3, 4, 6, 7, 9]