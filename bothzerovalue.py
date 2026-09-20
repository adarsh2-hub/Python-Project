try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("Invalid input or cannot divided by zero..")
finally:
    print("Program finished..")