#program to accept marks of 6 students and display them in sorted manner

marks = []
for i in range(6):
    mark = int(input(f"enter the marks of stduent {i}:"))
    marks.append(mark)

# marks.sort(reverse=True) , to sort in reverse (descending order)
marks.sort()
print(marks)