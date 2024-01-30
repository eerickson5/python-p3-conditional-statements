#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == 'admin' and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    string = ""
    if num % 3 == 0:
        string += "Fizz"
        print(num)
    if num % 5 == 0:
        string += "Buzz"
    if string == "":
        return num
    else:
        return string
    
def calculator(operation, num1, num2):
    operation_map={
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }
    if operation not in operation_map:
        print("Invalid operation!")
    return operation_map.get(operation, None)
