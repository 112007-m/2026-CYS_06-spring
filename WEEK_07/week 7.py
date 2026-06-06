
for i in range(1,10):
    for j in range(i):
        print("*",end="")
    print()



def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
show(5)





def factorial(n):
    if (n == 0 or n == 1)
        return 1:
    else:
        return n * factorial(n-1)
print(factorial(6))