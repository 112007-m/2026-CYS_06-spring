d = int(input("Enter a number: "))
for i in range(d):
    e = int(input("Enter roll number: "))
    f = int(input("Enter student number: "))
    a = int(input("Enter your marks: "))
    print("Roll number :",e)
    print("Student number :",f)
    print("Marks :",a)
b = 300
c = (a/b)*100
print(c)
if c >= 90:
    print("A+")
elif c>=85:
    print("A-")

elif c>=80:
    print("B+")
elif c>=75:
    print("B-")
elif c>=70:
    print("C+")
elif c>=65:
    print("C-")
elif c>=50:
    print("D")
else:
    print("F")