#check if "python" is present in log.txt or not

# with open("log.txt") as f:
#     content = f.read()
#     if"python" in content:
#         print("yes")
#     else:
#         print("no")
        
        
#check the line number where "python" is present

with open("/home/dushyant_new/python/file_input_output/problems/log.txt") as f:
    lines = f.readlines()
    
    lineno = 1
    for line in lines:
        if"python" in line:
            print(f"yes python is present in line number {lineno}")
            break
        lineno+=1
    else:
        print("not present")