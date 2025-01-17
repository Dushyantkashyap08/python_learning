with open("/home/dushyant_new/python/file_input_output/myfile.txt", "r") as f:
    print(f.read())
    
#while using with statement, we do not have to explicitly use f.close() function to close the file