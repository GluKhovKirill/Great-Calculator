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
    

def factorial(first):
    if (first == "ERR") or (first < 0):
        return "ERR"
    else:
        result = 1
        for i in range(1, first+1):
            result *= i
        return result
    

def raise_to_a_power(number, degree):
    if (number == "ERR") or (degree == "ERR"):
        return "ERR"
    else:
        return first ** degree
    
    
def square_root(number):
    if number < 0:
        return "ERR"
    return number ** 0.5