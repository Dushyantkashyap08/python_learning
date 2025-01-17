#read text from file named poem.txt and see if contains a word "twinkle" in it

with open("/home/dushyant_new/python/file_input_output/problems/poem.txt") as f:
    poem = f.read()
    if "twinkle" in poem:
        print("yes")
    else:
        print("no")