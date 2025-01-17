f = open("/home/dushyant_new/python/file_input_output/myfile.txt")
print("PRINT CONTENT OF THE FILE IN A LIST")
content = f.readlines()   
print(content)


print("\n PRINT LINES ONE BY ONE")
f = open("/home/dushyant_new/python/file_input_output/myfile.txt")
content = f.readline()
while content != "":
    print(content)
    content = f.readline()

f.close()