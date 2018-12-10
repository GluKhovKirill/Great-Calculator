import math


# Блок вычислительных функций

def amount(first, second):
    if (first == "ERR") or (second == "ERR"):
        return "ERR"
    else:
        return first + second
    

def difference(first, second):
    if (first == "ERR") or (first == "ERR"):
        return "ERR"
    else:
        return first - second
    

def multiply(first, second):
    if (first == "ERR") or (first == "ERR"):
        return "ERR"
    else:
        return first * second
    

def division(first, second):
    if (first == "ERR") or (second == "ERR") or (second == 0):
        return "ERR"
    else:
        return first / second    
    

def factorial(number):
    try:
        number = int(number)
        return math.factorial(number)
    except ValueError:
        return "ERR"
    except TypeError:
        return "ERR"
    

def raise_to_a_power(number, degree):
    if (number == "ERR") or (degree == "ERR"):
        return "ERR"
    else:
        return first ** degree
    
    
def square_root(number):
    if number < 0:
        return "ERR"
    return number ** 0.5


def module(number):
    return abs(number)


def in_decimal_system(number, base):
    try:
        return int(str(number), int(base))
    except ValueError:
        return "ERR"


def pi():
    return math.pi


def e():
    return math.e


def log(number, base=None):
    try:
        number = float(number)
        if base:
            base = float(base)
            return math.log(number, base)
        else:
            return math.log(number)
    except ValueError:
        return "ERR"


def degrees_to_radians(degrees):
    try:
        degrees = float(degrees)
        return degrees/360*math.pi*2
    except ValueError:
        return False


def radians_to_degrees(radians):
    try:
        radians = float(radians)
        degrees = (radians * 180) / pi()
        return degrees
    except ValueError:
        return False


def cosine(degrees):   
    radians = degrees_to_radians(degrees)
    if radians:
        return math.cos(radians)
    return False


def sine(degrees):
    radians = degrees_to_radians(degrees)
    if radians:
        return math.sin(radians)
    return False    


def tangent(degrees):
    radians = degrees_to_radians(degrees)
    if radians:
        return math.tan(radians)
    return False


