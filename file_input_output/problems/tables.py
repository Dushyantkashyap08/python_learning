
import os

def generateTable(n):
    directory = "tables_problem"
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables_problem/table_{n}.txt", "w") as f:
        f.write(table)




for i in range(2, 21):
    generateTable(i)