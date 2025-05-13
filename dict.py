d={'Alice':84,'SK':90}
n=input("Enter the student's name:")
if n in d:
    print(f"{n} marks:{d[n]}")
else:
    print("student not found")