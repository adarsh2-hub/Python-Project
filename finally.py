try:
    a=int(input("enter the first number:"))
    b=100
    print(100/a)
except ZeroDivisionError:
    print("cannot divided by zero!..")
finally:
    print("Thank you for using this program..")