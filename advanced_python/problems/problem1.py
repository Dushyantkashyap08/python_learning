#open 3 files and see if any of them is not present then print a custom message for the same

try:
    with(
        open("file_input_output/file.txt") as f1,
        open("file_input_output/myfile.txt") as f2,
        open("file_input_output/file1.txt") as f3 #this fiel does not exist 
    ):
        print(f1.read())
        print(f2.read())
except FileNotFoundError as fe:
    print(f"file not found {fe}")