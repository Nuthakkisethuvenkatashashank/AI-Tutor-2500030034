n=int(input("Enter no of entries:"))
student = {}
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    student[key]=value
print(student)