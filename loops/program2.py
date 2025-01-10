#program to greet all the persons in the following list whose name starts with s

names = ["rohan", "sachon", "dushyant", "sunil", "soham"]

for name in names:
    if name.startswith("s"):
        print(f"Namaste {name}")
    # if name[0].lower() == "s":      #another way without using startswith
    #     print(f"Namaste {name}")