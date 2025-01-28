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


#opening multiple files
f1 = open("/home/dushyant_new/python/file_input_output/myfile.txt")
f2 = open("/home/dushyant_new/python/file_input_output/file.txt")
f3 = open("/home/dushyant_new/python/file_input_output/file1.txt")

# or we can do like this :

with (
    open("/home/dushyant_new/python/file_input_output/myfile.txt") as f1,
    open("/home/dushyant_new/python/file_input_output/file.txt") as f2,
    open("/home/dushyant_new/python/file_input_output/file1.txt") as f3
):
    print(f1.read())
    print(f2.read())
    print(f3.read())

