#lambda functions are used to create fucntions using expression in a single line

# def square(n):   #trditional way
#     return n*n

square = lambda n:n*n  #in one line using lambda
even = lambda x : x%2==0 
add = lambda x,y : x+y

print(add(2,3))
print(even(5))
print(square(5))