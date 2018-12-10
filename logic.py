import math


# Блок вычислительных функций
# Короткие, но нужные функции
def pi(): return math.pi

def e(): return math.e

def module(number): return abs(number)


def amount(first, second):
    try:
        first, second = float(first), float(second)
        return first + second
    except ValueError:
        return False
    
    
def difference(first, second):
    try:
        first, second = float(first), float(second)
        return first - second
    except ValueError:
        return False


def multiply(first, second):
    try:
        first, second = float(first), float(second)
        return first * second
    except BaseException:
        return False
    

def division(first, second):
    try:
        first, second = float(first), float(second)
        return first / second
    except BaseException:
        return False    
    

def factorial(number):
    try:
        number = int(number)
        return math.factorial(number)
    except BaseException:
        return False
    

def raise_to_a_power(number, degree):
    try:
        return number ** degree
    except BaseException:
        return False
    
    
def square_root(number):
    if number < 0: return False
    try:
        return float(number) ** 0.5
    except ValueError:
        return False


def in_decimal_system(number, base):
    try:
        return int(str(number), int(base))
    except ValueError:
        return False


def log(number, base=None):
    try:
        number = float(number)
        if base:
            base = float(base)
            return math.log(number, base)
        else:
            return math.log(number)
    except ValueError:
        return False


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