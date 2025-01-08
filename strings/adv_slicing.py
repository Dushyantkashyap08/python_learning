word = 'amazing'
sliced = word[:3] # corresponds to [0:3]
sliced_2 = word[2:] # corresponds to [2:last_index]
print(sliced)
print(sliced_2)


#slicing while skiping
word = 'codinginpython'
sliced = word[1:7:2] # 3rd argument corresponds to the skip range means a gap of 2 here
print(sliced)