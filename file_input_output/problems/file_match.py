#check if content of 1 file matches with other or not

def file_match(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            return True
        else:
            return False
        

print(file_match("/home/dushyant_new/python/file_input_output/problems/this1.txt", "/home/dushyant_new/python/file_input_output/problems/this2.txt"))

