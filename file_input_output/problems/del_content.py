def deleteFile(file):
    with open(file, "w") as f:
        wipeout = f.write("")
        if wipeout:
            return "file wiped out successfully" 
        else: 
            return "file not wiped out"
        
file = deleteFile("/home/dushyant_new/python/file_input_output/problems/this2.txt")
print(file)