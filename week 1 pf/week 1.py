def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def permutation(n, r):
    return factorial(n) / factorial(n - r)

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

# Main program
n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("Permutation (nPr):", permutation(n, r))
print("Combination (nCr):", combination(n, r))








# Lambda to find larger number
large = lambda a, b: a if a > b else b

def table(num, limit):
    for i in range(1, limit+1):
        print(num, "x", i, "=", num*i)

# Main program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = large(a, b)
print("Largest number is:", largest)

limit = int(input("Enter table range: "))
table(largest, limit)








def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Main program
choice = input("Enter F for Fahrenheit to Celsius or C for Celsius to Fahrenheit: ")

if choice == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))
elif choice == 'C':
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))
else:
    print("Invalid choice")









def calculate_gpa():
    subjects = int(input("Enter number of subjects: "))

    total_grade_points = 0
    total_credit_hours = 0

    for i in range(subjects):
        print("\nSubject", i + 1)
        grade_point = float(input("Enter Grade Point: "))
        credit_hours = float(input("Enter Credit Hours: "))

        total_grade_points += grade_point * credit_hours
        total_credit_hours += credit_hours

    gpa = total_grade_points / total_credit_hours
    return gpa


# Main program
result = calculate_gpa()
print("\nYour GPA is:", round(result, 2))









# Lambda for uppercase
to_upper = lambda s: s.upper()

def invert(text):
    print("Reversed string:", text[::-1])

# Main program
s = input("Enter a string: ")

upper_text = to_upper(s)
print("Uppercase:", upper_text)

invert(upper_text)