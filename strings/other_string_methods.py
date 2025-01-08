#string methods

name = 'niharika coder'
print(len(name))  #find length of string
print(name.capitalize()) #capitalize only first character
print(name.count('d')) #returns the count of repeated characters in entire string
print(name.startswith('nih')) #returns boolean
print(name.endswith('der'))  #returns boolean
print(name.find('coder')) #returns index of the word in string and returns -1 if word not found
print(name.replace('coder', 'is a good girl')) #replaces a word in string


#replace() replaces multiple occurences of a same word in string
name = 'bhomik is a bad bad boy'
print(name.replace('bad', 'good'))