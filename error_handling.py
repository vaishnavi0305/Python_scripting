try:
    value = 10 / 0
    print(value)
except ZeroDivisionError:
    print("cannot divide by zero!")
finally:
    print("Script Finished")
