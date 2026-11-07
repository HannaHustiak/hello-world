a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))
operation = input("Обери дію (+, -, *, /): ")
if operation == "+":
    result = a + b
    print("Сума дорівнює:", result)
elif operation == "-":
    result = a - b
    print("Різниця дорівнює:", result)
elif operation == "*":
    result = a * b
    print("Добуток дорівнює:", result)
elif operation == "/":
    if b != 0:
        result = a / b
        print("Частка дорівнює:", result)
    else:
        print("На нуль ділити не можна!")

