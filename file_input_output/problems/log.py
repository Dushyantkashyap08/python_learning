#check if "python" is present in log.txt or not

# with open("log.txt") as f:
#     content = f.read()
#     if"python" in content:
#         print("yes")
#     else:
#         print("no")
        
        
#check the line number where "python" is present

with open("log.txt") as f:
    lines = f.readline()
    
    line = 1
    for line in lines:
        if"python" in line:
            print(f"yes python is present in line number {line}")
            break
        else:
            print("no")
        line+=1
    else:
        print("not present")