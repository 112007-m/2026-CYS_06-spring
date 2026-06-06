bytes_val = float(input("Enter bytes: "))

mb = bytes_val / (1024 * 1024)
gb = bytes_val / (1024 * 1024 * 1024)

print("Mega Bytes:", mb)
print("Giga Bytes:", gb)






ecat = float(input("Enter ECAT marks: "))
inter = float(input("Enter Intermediate marks: "))
matric = float(input("Enter Matric marks: "))

aggregate = (ecat * 0.33) + (inter * 0.50) + (matric * 0.17)

print("Aggregate is:", aggregate)








num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")









import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance:", distance)

# Function to find quadrant
def quadrant(x, y):
    if x > 0 and y > 0:
        return "1st Quadrant"
    elif x < 0 and y > 0:
        return "2nd Quadrant"
    elif x < 0 and y < 0:
        return "3rd Quadrant"
    elif x > 0 and y < 0:
        return "4th Quadrant"
    else:
        return "On Axis"

print("Point 1 is in:", quadrant(x1, y1))
print("Point 2 is in:", quadrant(x2, y2))











import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c   # Discriminant

# Nature of roots
if D == 0:
    print("Roots are real, equal and rational")
elif D > 0:
    print("Roots are real, distinct and irrational")
else:
    print("Roots are imaginary")

# Calculate roots
if D >= 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are:", root1, "and", root2)
else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are:", complex(real, imag), "and", complex(real, -imag))