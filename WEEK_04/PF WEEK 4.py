def greet():
    print("Welcome to Python Programming")

# Main program
greet()
greet()




def displayName(name):
    print("Hello", name)

# Main program
displayName("Ali")






def addNumbers(a, b):
    return a + b

# Main program
result = addNumbers(5, 3)
print("Sum is:", result)






def square(num):
    return num * num

# Main program
result = square(4)
print("Square is:", result)






def power(base, exponent=2):
    return base ** exponent

# Main program
print(power(5))       # default exponent (square)
print(power(5, 3))    # custom exponent





def student(name, age):
    print("Name:", name)
    print("Age:", age)

# Main program (keyword arguments)
student(name="Ali", age=20)








def maximum(a, b, c):
    return max(a, b, c)

# Main program
print("Maximum is:", maximum(3, 7, 5))






def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Total is:", sum)

# Main program
total(1, 2, 3, 4, 5)







def average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    avg = sum / len(numbers)
    print("Average is:", avg)

# Main program
average(10, 20, 30, 40)







def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Main program
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")
    








