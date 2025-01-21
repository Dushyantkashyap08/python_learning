import time

with open("/home/dushyant_new/python/file_input_output/problems/donkey.txt", "r") as f:
    content = f.read()
    print(content)

    updated_content = content.replace("Donkey", "Monkey")
    print("UPDATING THE CONTENT IN THE FILE...")
    time.sleep(5)
    print("FILE UPDATED")
    with open("/home/dushyant_new/python/file_input_output/problems/donkey.txt", "w") as f:
        f.write(updated_content)
        print(updated_content)
        
        
        
#same problem with multiple words
# words = ['bhai', 'bad', 'donkey']

# with open("donkey.txt", "r") as f:
#     content = f.read()
#     print(content)

#     for word in words:
#         content = content.replace(word, "#"*len(word))
   
#     print("UPDATING THE CONTENT IN THE FILE...")
#     time.sleep(5)
#     print("FILE UPDATED")
#     with open("donkey.txt", "w") as f:
#         f.write(content)
#         print(content)