#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum


def halve(number):
    halved = number / 2
    print(halved)
    return halved


greet_programmer()
greet("Alice")
greet_with_default()
add(55, 108)
halve(10)

