

# Open the file in read mode and read its content
with open("/home/dushyant_new/python/file_input_output/file.txt", "r") as f:
    content = f.read()

# Modify the content
updated_content = content.replace("hello", "new_text")

# Write the updated content back to the file
with open("/home/dushyant_new/python/file_input_output/file.txt", "w") as f:
    f.write(updated_content)
