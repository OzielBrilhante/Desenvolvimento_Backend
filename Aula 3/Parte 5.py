try:
    print(100/0)

except ZeroDivisionError as error:
    print(error)
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
else:
    print("Execute novamente o programa!")
