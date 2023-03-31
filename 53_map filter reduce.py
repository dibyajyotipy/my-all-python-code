# MAP
l = [1,5,3,3,6,9]
newl=list(map(lambda x: x*x*x, l))
print(newl)


# FILTER 
def filter_function(x):
    return x>2
newnewl=list(filter(filter_function, l))
print(newnewl)


# REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
print(sum)