import math

def quadratic_equation_solver(a,b,c):
    result1 = float((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
    result2 = float((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
    print(f"x1 is: {result1} x2 is: {result2}")
    

quadratic_equation_solver(1, -5, 2)





