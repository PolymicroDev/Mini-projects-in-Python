import math

def quadratic_equation_solver(a,b,c):
    root1 = float((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
    root2 = float((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
    return print(f"x1 is: {root1} x2 is: {root2}")
    

quadratic_equation_solver(1, -5, 2)





