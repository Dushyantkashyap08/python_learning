#file I/O : python can read data from any file and write data into it

#file is a collection of data that is stored in a particular location in hard disk
#RAM is volatile memory so data cannot be stored permanently
#file is a permanent storage

f = open("/home/dushyant_new/python/file_input_output/file.txt")
print(f.read())
f.close()