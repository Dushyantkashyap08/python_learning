with open("/home/dushyant_new/python/file_input_output/problems/this1.txt") as f:
    content = f.read()
    
    with open("/home/dushyant_new/python/file_input_output/problems/this2.txt", "w") as f:
        content = f.write(content)
        if content:
            print("content copied successfully")
        else:
            print("content not copied")