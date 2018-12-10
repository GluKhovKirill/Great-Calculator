import math



def pi(): return math.pi

def e(): return math.e

def module(number): return abs(number)


def amount(first, second):
    # Сумма (<first> + <second>)
    try:
        first, second = float(first), float(second)
        return first + second
    except ValueError:
        return False
    
    
def difference(first, second):
    # Разность (<first> - <second>)
    try:
        first, second = float(first), float(second)
        return first - second
    except ValueError:
        return False


def multiply(first, second):
    # Произведение (<first> * <second>)
    try:
        first, second = float(first), float(second)
        return first * second
    except BaseException:
        return False
    

def division(first, second):
    # Частное (<first> / <second>)
    try:
        first, second = float(first), float(second)
        return first / second
    except BaseException:
        return False    
    

def factorial(number):
    # Получение факториала (<number>!)
    try:
        number = int(number)
        return math.factorial(number)
    except BaseException:
        return False
    

def raise_to_a_power(number, degree):
    # Возведение в степень (<number>^<degree>)
    try:
        return number ** degree
    except BaseException:
        return False
    
    
def square_root(number):
    # Извлечение квадратного корня
    if number < 0: return False
    try:
        return float(number) ** 0.5
    except ValueError:
        return False


def in_decimal_system(number, base):
    # Перевод в десятичную систему счисления, 
    # где число - <number>, а <base> - система счисления
    try:
        return int(str(number), int(base))
    except ValueError:
        return False


def log(number, base=None):
    # Получение логарифма <number> по основанию <base>
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
    # Перевод градусов в радианы
    try:
        degrees = float(degrees)# Ïðîèçâåäåíèå (<first> * <second>)
        return degrees/360*math.pi*2
    except ValueError:
        return False


def radians_to_degrees(radians):
    # Перевод радианов в градусы
    try:
        radians = float(radians)
        degrees = (radians * 180) / pi()
        return degrees
    except ValueError:
        return False


def cosine(radians, is_degree=False):   
    # Косинус
    if is_degree:
        radians = degrees_to_radians(degrees)
    if radians:
        return math.cos(radians)
    return False


def sine(radians, is_degree=False):
    # Синус
    if is_degree:
        radians = degrees_to_radians(degrees)
    if radians:
        return math.sin(radians)
    return False    


def tangent(radians, is_degree=False):
    # Тангенс
    if is_degree:
        radians = degrees_to_radians(degrees)
    if radians:
        return math.tan(radians)
    return False