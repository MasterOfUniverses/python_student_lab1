import math

def lab_fn(a,b,c):
    d=float(b*b - 4*a*c)
    if d<0:
        return (int(0),float(0),float(0))
    else:
        x_1=float((b+math.sqrt(d))/(2*a))
        x_2=float((b-math.sqrt(d))/(2*a))
        return (int(1),x_1,x_2)

print("Please, enter parameters of equation ax^2 + bx + c:")        
a=float(input("Enter a:\n"))
b=float(input("Enter b:\n"))
c=float(input("Enter c:\n"))
has_roots,x_1,x_2 = lab_fn(a,b,c)
if has_roots==0:
    print("Equation has no real roots!")
else:
    print(f"Roots of this equation {a}*x^2 + {b}*x + {c} is {x_1} and {x_2}")
    
