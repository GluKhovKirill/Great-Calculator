import math


class MathExecutor:
    def __init__(self, first, operand, second):
        self.error_codes = {"ERR" : "Что-то пошло не так!",
                            "NONE": "Не передан необходимый операнд",
                            "NFLT": "Операнд не является числом",
                            "NINT": "Операнд не является целочисленным числом (integer)",
                            "ZERODIV": "Вы попытались поделить на 0. К сожалению,это невозможно!",
                            "OPS": "Ошибка в действиях...."}
        self.equation = (first, operand, second)
    
    def execute(self):
        #"5+5*6-9"
        operantors = {"+": self.amount,
                    "-": self.difference,
                    "*": self.multiply,
                    "/": self.division,
                    "|": self.module,
                    "\u03C0": self.pi,
                    "\u0190": self.e,
                    "!": self.factorial,
                    "^": self.raise_to_a_power,
                    "\u221A": self.square_root,
                    "log": self.log,
                    "nToTen": self.in_decimal_system,
                    "ToRad": self.degrees_to_radians,
                    "ToDeg": self.radians_to_degrees,
                    "cos": self.cosine,
                    "sin": self.sine,
                    "tg": self.tangent,
                    "ctg": self.cotangent}
        
        first, operator, second = self.equation
        if operand in operands:
            return operators[operator](first, second)
        else:
            return (False, "OPS")
         
    def pi(self, first, second): return math.pi

    def e(self, first, second): return math.e

    def module(self, number, nothing):
        #Модуль
        try:
            number = float(number)
            return (True, abs(number))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")

    def amount(self, first, second):
        # Сумма (<first> + <second>)
        try:
            first = float(first)
            second = float(second)
            return (True, (first + second))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")        
      
    def difference(self, first, second):
        # Разность (<first> - <second>)
        try:
            first = float(first)
            second = float(second)
            return (True, (first - second))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")        

    def multiply(self, first, second):
        # Произведение (<first> * <second>)
        try:
            first = float(first)
            second = float(second)
            return (True, first * second)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")        
    
    def division(self, first, second):
        # Частное (<first> / <second>)
        try:
            first, second = float(first), float(second)
            return (True, first / second)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")        
        except ZeroDivisionError:
            return (False, "ZERODIV")
        except BaseException:
            return (False, "ERR")   
    
    def factorial(self, number, nothing):
        # Получение факториала (<number>!)
        try:
            if not str(number).isdigit():
                raise ValueError
            number = int(number)
            return (True, math.factorial(number))
        except ValueError:
            return (False, "NINT")
        except TypeError:
            return (False, "NONE")         
        except BaseException:
            return (False, "ERR")
    
    def raise_to_a_power(self, number, degree):
        # Возведение в степень (<number>^<degree>)
        try:
            return (True, number ** degree)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE") 
        except BaseException:
            return (False, "ERR")
                 
    def square_root(self, number, nothing):
        # Извлечение квадратного корня
        if number < 0: return False
        try:
            return (True, float(number) ** 0.5)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE") 
        except BaseException:
            return (False, "ERR")        

    def in_decimal_system(self, number, base):
        # Перевод в десятичную систему счисления, 
        # где число - <number>, а <base> - система счисления
        try:
            return (True, int(str(number), int(base)))
        except ValueError:
            return (False, "NINT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")        
            
    def log(self, number, base=None):
        # Получение логарифма <number> по основанию <base>
        try:
            number = float(number)
            if base:
                base = float(base)
                return (True, math.log(number, base))
            else:
                return math.log(number)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR") 
                     
    def degrees_to_radians(self, degrees, nothing):
        # Перевод градусов в радианы
        try:
            degrees = float(degrees)
            return (True, degrees/360*math.pi*2)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")
                   
    def radians_to_degrees(self, radians, nothing):
        # Перевод радианов в градусы
        try:
            radians = float(radians)
            degrees = (radians * 180) / pi()
            return (True, degrees)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")
            
    def cosine(self, radians, nothing, is_degree=False):   
        # Косинус
        if is_degree:
            radians = degrees_to_radians(degrees)
        if radians[0]:
            return (True, math.cos(radians[1]))
        return radians           
            
    def sine(self, radians, nothing, is_degree=False):
        # Синус
        if is_degree:
            radians = degrees_to_radians(degrees)
        if radians[0]:
            return (True, math.sin(radians[1]))
        return radians   
             
    def tangent(self, radians, nothing, is_degree=False):
        # Тангенс
        if is_degree:
            radians = degrees_to_radians(degrees)
        if radians[0]:
            return (True, math.tan(radians[1]))
        return radians
    
    def cotangent(self, radians, nothing, is_degree=False):
        tng = self.tangent(radians, second, is_degrees)
        if tng[0]:
            return (True, 1/tng[1])
        return tng