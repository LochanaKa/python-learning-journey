try:
    print("Begin")
    result=10/0
    print("Calculated")
except ZeroDivisionError:
    print("Division Failed!")
finally:
    print("Check Finished")
print('Next Task')