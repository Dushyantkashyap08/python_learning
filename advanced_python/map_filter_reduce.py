#map function is used to APPLY A METHOD TO EACH ITEM in a list or a tuple

l = [1,2,3,4,5,6]

square = lambda x: x*x
sqList = map(square, l)
print(list(sqList)) 


#filter function is used to FILTER OUT ITEMS from a list based on a function

l = [1,2,3,4,5,6]

even = lambda x: x%2==0
evens = filter(even, l)
print(list(evens))


#reduce fucntion is used to REDUCE a list to a single value

from functools import reduce #we have to import reduce to use it
l = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, l) #x=1 y=2 then result of x+y adds up with the next num and so on untill the list is completed
print(sum)