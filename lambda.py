# Lambda
# one line unnamed function
# useful if you only need a function once in your code, or used in higher order functions

# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))
# same as
def add10_func(x):
    return x + 10

mult = lambda x,y: x * y
print(mult(5,5))

# sorted function
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) # sort according to x index
points2D_sorted_key = sorted(points2D, key=lambda x: x[1]) # sort according to y index
points2D_sorted_key_sum = sorted(points2D, key=lambda x: x[0] + x[1]) # sort by sum of x, y
print(points2D)
print(points2D_sorted)
print(points2D_sorted_key)
print(points2D_sorted_key_sum)
# same as sort by y index
def sort_by_y(x):
    return x[1]

# map function          map(func, seq)
# transforms each element with a function
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
# list comprehension version
c = [x*2 for x in a]
print(c)

# filter function       filter(func, seq) 
# returns all elements to which the function returns True
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a) # only even numbers
print(list(b))
# list comprehension version
c = [x for x in a if x%2==0]
print(c)

# reduce function       reduce(func, seq)
# repeatedly applies the function to the values and returns a single value
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x,y: x*y, a)  # 1*2=2, 2*3=6, 6*4=24
print(product_a)
