import math


class MathExecutor:
    def __init__(self, first, operand, second, is_degree):
        self.error_codes = {"ERR" : "Что-то пошло не так!",
                            "NONE": "Не передан необходимый операнд",
                            "NFLT": "Операнд не является числом",
                            "NINT": "Операнд не является целочисленным числом (integer)",
                            "ZERODIV": "Вы попытались поделить на 0. К сожалению,это невозможно!",
                            "OPS": "Я не могу это выполинть...",
                            "NINT-nToTen": "Операнд не является целочисленным числом (integer) или такое число невозможно в данной системе"}
        self.equation = (first, operand, second, is_degree)
    
    def execute(self):
        #"5+5*6-9"
        operators = {"+": self.amount,
                    "-": self.difference,
                    "*": self.multiply,
                    ":": self.division,
                    "|x|": self.module,
                    "+ -": self.invert_number,
                    "\u03C0": self.pi,
                    "\u0190": self.e,
                    "n!": self.factorial,
                    "x^n": self.raise_to_a_power,
                    "2"+"\u221A"+"x": self.square_root,
                    "3"+"\u221A"+"x": self.cube_root,
                    "log": self.log,
                    "n to10": self.in_decimal_system,
                    "ToRad": self.degrees_to_radians,
                    "ToDeg": self.radians_to_degrees,
                    "cos": self.cosine,
                    "sin": self.sine,
                    "tg": self.tangent,
                    "ctg": self.cotangent,
                    "x^2": self.x_in_square,
                    "x^3": self.x_in_cube,
                    "10^x": self.ten_in_x,
                    "2^x": self.two_in_x,
                    "1/x": self.one_div_x,
                    "log": self.log,
                    "Rad<->Deg": self.convert_units,
                    "%": self.percents,
                    "*100 (un%)": self.un_percents}
        
        first, operator, second, is_degree = self.equation
        if operator in operators:
            answer = operators[operator](first, second, is_degree)
            # print("ANS:",answer)
            if answer[0]:
                return str(answer[1])
            else:
                return self.error_codes[answer[1]]
        else:
            # print(operator)
            return self.error_codes["OPS"]
         
    def pi(self, *nothing): return (True, math.pi)

    def e(self, *nothing): return (True, math.e)
    
    def invert_number(self, number, *nothing):
        try:
            return (True, -float(number))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")    

    def module(self, number, *nothing):
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

    def amount(self, first, second, *nothing):
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
      
    def difference(self, first, second, *nothing):
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

    def multiply(self, first, second, *nothing):
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
    
    def division(self, first, second, *nothing):
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
    
    def factorial(self, number, *nothing):
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
    
    def raise_to_a_power(self, number, degree, *nothing):
        # Возведение в степень (<number>^<degree>)
        try:
            return (True, float(number) ** float(degree))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE") 
        except BaseException:
            return (False, "ERR")
                 
    def square_root(self, number, *nothing):
        # Извлечение квадратного корня
        
        try:
            number = float(number)
            if number < 0:
                return False
            return (True, number ** 0.5)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE") 
        except BaseException:
            return (False, "ERR")        

    def in_decimal_system(self, number, base, *nothing):
        # Перевод в десятичную систему счисления, 
        # где число - <number>, а <base> - система счисления
        try:
            return (True, int(str(number), int(base)))
        except ValueError:
            return (False, "NINT-nToTen")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")        
            
    def log(self, number, base=None, *nothing):
        # Получение логарифма <number> по основанию <base>
        try:
            number = float(number)
            if base:
                base = float(base)
                return (True, math.log(number, base))
            else:
                return (True, math.log(number))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR") 
                     
    def degrees_to_radians(self, degrees, *nothing):
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
                   
    def radians_to_degrees(self, radians, *nothing):
        # Перевод радианов в градусы
        try:
            radians = float(radians)
            pi = self.pi()[1]
            degrees = (radians * 180) / pi
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
            radians = self.degrees_to_radians(radians)[1]
        try:
            radians = float(radians)
            return (True, math.cos(radians)) 
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")         
                  
            
    def sine(self, radians, nothing, is_degree=False):
        # Синус
        if is_degree:
            radians = self.degrees_to_radians(radians)[1]
        try:
            radians = float(radians)
            return (True, math.sin(radians))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")  
        except BaseException:
            return (False, "ERR")         

             
    def tangent(self, radians, nothing, is_degree=False):
        # Тангенс
        if is_degree:
            radians = self.degrees_to_radians(radians)[1]
        else:
            try:
                radians = float(radians)
            except ValueError:
                return (False, "NFLT")
            except TypeError:
                return (False, "NONE")  
            except BaseException:
                return (False, "ERR")                    
            
        if radians:
            return (True, math.tan(radians))
        return (True, radians)
    
    def cotangent(self, radians, nothing, is_degree=False):
        tng = self.tangent(radians, nothing, is_degree)
        if tng[0]:
            return (True, 1/tng[1])
        return tng
    
    def x_in_square(self, number, *nothing):
        return self.raise_to_a_power(number, 2)
    
    def x_in_cube(self, number, *nothing):
        return self.raise_to_a_power(number, 3)
    
    def two_in_x(self, number, *nothing):
        return self.raise_to_a_power(2, number)
    
    def ten_in_x(self, number, *nothing):
        return self.raise_to_a_power(10, number)
    
    def cube_root(self, number, *nothing):
        try:
            number = float(number)
            return (True, number ** (1/3))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE") 
        except BaseException:
            return (False, "ERR") 
    
    def one_div_x(self, number, *nothing):
        try:
            return (True, 1 / float(number))
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")         
    #ВАЛИДНО ^
    
    def convert_units(self, first, nothing, is_degree=False):
        #print(first, is_degree)
        if is_degree:
            return self.degrees_to_radians(first)
        return self.radians_to_degrees(first)
    
    def percents(self, number, *nothing):
        try:
            number = float(number)
            perc = number * 100
            perc = str(perc) + "%"
            return (True, perc)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")  
    
    def un_percents(self, perc, *nothing):
        try:
            perc = float(perc.replace("%", ""))
            num = perc / 100
            return (True, num)
        except ValueError:
            return (False, "NFLT")
        except TypeError:
            return (False, "NONE")
        except BaseException:
            return (False, "ERR")        