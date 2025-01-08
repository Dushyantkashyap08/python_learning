#slicing of stings (done using indexing method)

name = "niharika"
nameshort = name[0:3] #syntax : [start_index : end_index] , slicing will start from start_index to end_index excluding end_index
nameshort_2 = name[-1:-4]#using negative indexing ,- However, in slicing, the start index (`-1`) must be less than the end index (`-4`) for it to slice in the forward direction. Since `-1 > -4`, the result is an **empty string**.
nameshort_3 = name[-4:-1]
print(name)
print(nameshort)
print(nameshort_2) #output will be empty string
print(nameshort_3) #correct output

print(name[2]) #accessing a char from string


#slicing in reverse order in negative indexing
name = 'dushyant'
sliced = name[-1:-4:-1] #3rd argument represents slicing in reverse order 
print (sliced)