d = int(input("Enter a number of students: "))
i = 1
while i<=d:
    e = int(input("Enter roll number: "))
    f = input("enter student name: ")
    a =int(input("Enter your marks: "))
    print("Roll no:",e)
    print("Student name:",f)
    print("your marks:",a)
b = 300
c = (a/b)*100
print(c)
if c >=90:
    print("A+")
elif c >=85:
    print("A")
elif c >=80:
    print("B+")
elif c >=75:
    print("B")
elif c >=70:
    print("C+")
elif c >=65:
    print("C_")
elif c >=60:
    print("D+")
elif c >=50:
    print("D-")
else:
    print("F")
i = i+1